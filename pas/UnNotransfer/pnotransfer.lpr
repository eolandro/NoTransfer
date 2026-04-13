program pnotransfer;

{$mode objfpc}{$H+}

uses
  {$IFDEF UNIX}
  cthreads,
  {$ENDIF}
  Classes, SysUtils, CustApp,md5
  { you can add units after this };

type

  { TUnNotransfer }

  TUnNotransfer = class(TCustomApplication)
  protected
    procedure DoRun; override;
  private
    ready : integer;
    ifile : String;
    ofile : String;
    sifile : TFileStream;
    sofile : TFileStream;
  public
    constructor Create(TheOwner: TComponent); override;
    destructor Destroy; override;
    procedure WriteHelp; virtual;
  end;

{ TUnNotransfer }

procedure TUnNotransfer.DoRun;
var
  ErrorMsg: String;
  i : byte;
  j : integer;
  oContext: TMD5Context;
  tContext: TMD5Context;
  DigestT: TMD5Digest;
  DigestF: TMD5Digest;
  oneByte: byte;
  verbose: boolean;
begin
  ready := 0;
  j := 0;
  verbose := false;
  // quick check parameters
  {
  ErrorMsg:=CheckOptions('h', 'help');
  if ErrorMsg<>'' then begin
    ShowException(Exception.Create(ErrorMsg));
    Terminate;
    Exit;
  end;
  }
  // parse parameters
  if HasOption('h', 'help') then begin
    WriteHelp;
    Terminate;
    Exit;
  end;

  { add your program here }
  // parse parameters
  if HasOption('i', 'inputfileNT') then begin
    ifile :=  GetOptionValue('i', 'inputfileNT');
    if FileExists(ifile) then
    begin
      ready := ready + 1;
    end;
  end;
  if HasOption('o', 'outputfile') then begin
    ofile :=  GetOptionValue('o', 'outputfile');
    if not FileExists(ofile) then
    begin
      ready := ready + 1;
    end;
  end;
  if HasOption('v', 'verbose') then begin
    verbose := True;
  end;
  if ready = 2 then begin
    sifile := TFileStream.Create(ifile, fmOpenRead or fmShareDenyWrite);
    sofile := TFileStream.Create(ofile, fmCreate);
    MD5Init(oContext);
    try
      while sifile.Position < sifile.Size do begin
          tContext := oContext;
          sifile.Read (DigestF[0],16);
          for i:= 0 to 255 do begin
              oneByte := i;
              MD5Update(tContext,oneByte,1);
              MD5Final(tContext, DigestT);
              if CompareByte(DigestT,DigestF,16) = 0 then
              begin
                MD5Update(oContext,oneByte,1);
                sofile.Write(onebyte,1);
                if verbose then
                begin
                  writeln(j);
                end;
                j := j + 1;
                break;
              end
              else begin
                tContext := oContext;
              end;

          end;
      end;
    finally
      sifile.Free;
      sofile.Free;
    end;
     writeln('Ok');
  end
  else begin
    WriteHelp;
    Terminate;
    Exit;
  end;
  // stop program loop
  Terminate;
end;

constructor TUnNotransfer.Create(TheOwner: TComponent);
begin
  inherited Create(TheOwner);
  StopOnException:=True;
end;

destructor TUnNotransfer.Destroy;
begin
  inherited Destroy;
end;

procedure TUnNotransfer.WriteHelp;
begin
  { add your help code here }
  writeln('Usage: ', ExeName, ' -h');
end;

var
  Application: TUnNotransfer;
begin
  Application:=TUnNotransfer.Create(nil);
  Application.Title:='UnNoTransferpas';
  Application.Run;
  Application.Free;
end.

