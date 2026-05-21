[Setup]
AppName=Gerenciador de Tarefas
AppVersion=1.0
DefaultDirName={autopf}\GerenciadorDeTarefas
DefaultGroupName=Gerenciador de Tarefas
OutputDir=setup_out
OutputBaseFilename=Instalador_Tarefas_Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Files]
; O Inno Setup vai buscar o executável gerado pelo PyInstaller dentro da pasta dist
Source: "dist\app.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Gerenciador de Tarefas"; Filename: "{app}\app.exe"
Name: "{autodesktop}\Gerenciador de Tarefas"; Filename: "{app}\app.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Criar um atalho na Área de Trabalho"; Flags: unchecked