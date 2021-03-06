import dovado.vivado_interaction as v


vivado = None
available_parts = [
    "xc7k70tfbv676-1",
    "xc7k70tfbv676-2",
    "xc7k70tfbv676-2L",
    "xc7k70tfbv676-3",
    "xc7k70tfbv484-1",
    "xc7k70tfbv484-2",
    "xc7k70tfbv484-2L",
    "xc7k70tfbv484-3",
    "xc7k70tfbg676-1",
    "xc7k70tfbg676-2",
    "xc7k70tfbg676-2L",
    "xc7k70tfbg676-3",
    "xc7k70tfbg484-1",
    "xc7k70tfbg484-2",
    "xc7k70tfbg484-2L",
    "xc7k70tfbg484-3",
    "xc7k160tfbg484-1",
    "xc7k160tfbg484-2",
    "xc7k160tfbg484-2L",
    "xc7k160tfbg484-3",
    "xc7k160tfbg676-1",
    "xc7k160tfbg676-2",
    "xc7k160tfbg676-2L",
    "xc7k160tfbg676-3",
    "xc7k160tfbv484-1",
    "xc7k160tfbv484-2",
    "xc7k160tfbv484-2L",
    "xc7k160tfbv484-3",
    "xc7k160tfbv676-1",
    "xc7k160tfbv676-2",
    "xc7k160tfbv676-2L",
    "xc7k160tfbv676-3",
    "xc7k160tffg676-1",
    "xc7k160tffg676-2",
    "xc7k160tffg676-2L",
    "xc7k160tffg676-3",
    "xc7k160tffv676-1",
    "xc7k160tffv676-2",
    "xc7k160tffv676-2L",
    "xc7k160tffv676-3",
    "xc7k160tifbv676-2L",
    "xc7k160tifbg484-2L",
    "xc7k160tifbg676-2L",
    "xc7k160tifbv484-2L",
    "xc7k160tiffv676-2L",
    "xc7k160tiffg676-2L",
    "xc7k70tlfbv676-2L",
    "xc7k70tlfbv484-2L",
    "xc7k70tlfbg676-2L",
    "xc7k70tlfbg484-2L",
    "xc7k160tlfbg484-2L",
    "xc7k160tlfbg676-2L",
    "xc7k160tlfbv484-2L",
    "xc7k160tlfbv676-2L",
    "xc7k160tlffg676-2L",
    "xc7k160tlffv676-2L",
    "xc7a12ticsg325-1L",
    "xc7a12ticpg238-1L",
    "xc7a12tcsg325-1",
    "xc7a12tcsg325-2",
    "xc7a12tcsg325-2L",
    "xc7a12tcsg325-3",
    "xc7a12tcpg238-1",
    "xc7a12tcpg238-2",
    "xc7a12tcpg238-2L",
    "xc7a12tcpg238-3",
    "xc7a25tcpg238-1",
    "xc7a25tcpg238-2",
    "xc7a25tcpg238-2L",
    "xc7a25tcpg238-3",
    "xc7a25tcsg325-1",
    "xc7a25tcsg325-2",
    "xc7a25tcsg325-2L",
    "xc7a25tcsg325-3",
    "xc7a25ticpg238-1L",
    "xc7a25ticsg325-1L",
    "xc7a50tcsg324-1",
    "xc7a50tcsg324-2",
    "xc7a50tcsg324-2L",
    "xc7a50tcsg324-3",
    "xc7a50tcpg236-1",
    "xc7a50tcpg236-2",
    "xc7a50tcpg236-2L",
    "xc7a50tcpg236-3",
    "xc7a50tcsg325-1",
    "xc7a50tcsg325-2",
    "xc7a50tcsg325-2L",
    "xc7a50tcsg325-3",
    "xc7a50tfgg484-1",
    "xc7a50tfgg484-2",
    "xc7a50tfgg484-2L",
    "xc7a50tfgg484-3",
    "xc7a50tftg256-1",
    "xc7a50tftg256-2",
    "xc7a50tftg256-2L",
    "xc7a50tftg256-3",
    "xc7a35tiftg256-1L",
    "xc7a35tifgg484-1L",
    "xc7a35ticsg325-1L",
    "xc7a35ticsg324-1L",
    "xc7a35ticpg236-1L",
    "xc7a50ticpg236-1L",
    "xc7a50tiftg256-1L",
    "xc7a50tifgg484-1L",
    "xc7a50ticsg325-1L",
    "xc7a50ticsg324-1L",
    "xc7a35tftg256-1",
    "xc7a35tftg256-2",
    "xc7a35tftg256-2L",
    "xc7a35tftg256-3",
    "xc7a35tfgg484-1",
    "xc7a35tfgg484-2",
    "xc7a35tfgg484-2L",
    "xc7a35tfgg484-3",
    "xc7a35tcsg325-1",
    "xc7a35tcsg325-2",
    "xc7a35tcsg325-2L",
    "xc7a35tcsg325-3",
    "xc7a35tcsg324-1",
    "xc7a35tcsg324-2",
    "xc7a35tcsg324-2L",
    "xc7a35tcsg324-3",
    "xc7a35tcpg236-1",
    "xc7a35tcpg236-2",
    "xc7a35tcpg236-2L",
    "xc7a35tcpg236-3",
    "xc7a15tcpg236-1",
    "xc7a15tcpg236-2",
    "xc7a15tcpg236-2L",
    "xc7a15tcpg236-3",
    "xc7a15tcsg324-1",
    "xc7a15tcsg324-2",
    "xc7a15tcsg324-2L",
    "xc7a15tcsg324-3",
    "xc7a15tcsg325-1",
    "xc7a15tcsg325-2",
    "xc7a15tcsg325-2L",
    "xc7a15tcsg325-3",
    "xc7a15tfgg484-1",
    "xc7a15tfgg484-2",
    "xc7a15tfgg484-2L",
    "xc7a15tfgg484-3",
    "xc7a15tftg256-1",
    "xc7a15tftg256-2",
    "xc7a15tftg256-2L",
    "xc7a15tftg256-3",
    "xc7a15ticpg236-1L",
    "xc7a15ticsg324-1L",
    "xc7a15ticsg325-1L",
    "xc7a15tifgg484-1L",
    "xc7a15tiftg256-1L",
    "xc7a75tfgg484-1",
    "xc7a75tfgg484-2",
    "xc7a75tfgg484-2L",
    "xc7a75tfgg484-3",
    "xc7a75tfgg676-1",
    "xc7a75tfgg676-2",
    "xc7a75tfgg676-2L",
    "xc7a75tfgg676-3",
    "xc7a75tftg256-1",
    "xc7a75tftg256-2",
    "xc7a75tftg256-2L",
    "xc7a75tftg256-3",
    "xc7a75tcsg324-1",
    "xc7a75tcsg324-2",
    "xc7a75tcsg324-2L",
    "xc7a75tcsg324-3",
    "xc7a75ticsg324-1L",
    "xc7a75tifgg484-1L",
    "xc7a75tifgg676-1L",
    "xc7a75tiftg256-1L",
    "xc7a100tiftg256-1L",
    "xc7a100tifgg676-1L",
    "xc7a100tifgg484-1L",
    "xc7a100ticsg324-1L",
    "xc7a100tftg256-1",
    "xc7a100tftg256-2",
    "xc7a100tftg256-2L",
    "xc7a100tftg256-3",
    "xc7a100tfgg676-1",
    "xc7a100tfgg676-2",
    "xc7a100tfgg676-2L",
    "xc7a100tfgg676-3",
    "xc7a100tfgg484-1",
    "xc7a100tfgg484-2",
    "xc7a100tfgg484-2L",
    "xc7a100tfgg484-3",
    "xc7a100tcsg324-1",
    "xc7a100tcsg324-2",
    "xc7a100tcsg324-2L",
    "xc7a100tcsg324-3",
    "xc7a200tfbg484-1",
    "xc7a200tfbg484-2",
    "xc7a200tfbg484-2L",
    "xc7a200tfbg484-3",
    "xc7a200tfbg676-1",
    "xc7a200tfbg676-2",
    "xc7a200tfbg676-2L",
    "xc7a200tfbg676-3",
    "xc7a200tfbv484-1",
    "xc7a200tfbv484-2",
    "xc7a200tfbv484-2L",
    "xc7a200tfbv484-3",
    "xc7a200tfbv676-1",
    "xc7a200tfbv676-2",
    "xc7a200tfbv676-2L",
    "xc7a200tfbv676-3",
    "xc7a200tffg1156-1",
    "xc7a200tffg1156-2",
    "xc7a200tffg1156-2L",
    "xc7a200tffg1156-3",
    "xc7a200tsbv484-1",
    "xc7a200tsbv484-2",
    "xc7a200tsbv484-2L",
    "xc7a200tsbv484-3",
    "xc7a200tffv1156-1",
    "xc7a200tffv1156-2",
    "xc7a200tffv1156-2L",
    "xc7a200tffv1156-3",
    "xc7a200tsbg484-1",
    "xc7a200tsbg484-2",
    "xc7a200tsbg484-2L",
    "xc7a200tsbg484-3",
    "xc7a200tisbv484-1L",
    "xc7a200tisbg484-1L",
    "xc7a200tiffv1156-1L",
    "xc7a200tiffg1156-1L",
    "xc7a200tifbv676-1L",
    "xc7a200tifbv484-1L",
    "xc7a200tifbg676-1L",
    "xc7a200tifbg484-1L",
    "xc7a12tlcsg325-2L",
    "xc7a12tlcpg238-2L",
    "xc7a25tlcsg325-2L",
    "xc7a25tlcpg238-2L",
    "xc7a35tlcpg236-2L",
    "xc7a35tlcsg324-2L",
    "xc7a35tlcsg325-2L",
    "xc7a35tlfgg484-2L",
    "xc7a35tlftg256-2L",
    "xc7a15tlcpg236-2L",
    "xc7a15tlcsg324-2L",
    "xc7a15tlcsg325-2L",
    "xc7a15tlfgg484-2L",
    "xc7a15tlftg256-2L",
    "xc7a50tlcpg236-2L",
    "xc7a50tlcsg324-2L",
    "xc7a50tlcsg325-2L",
    "xc7a50tlfgg484-2L",
    "xc7a50tlftg256-2L",
    "xc7a75tlftg256-2L",
    "xc7a75tlfgg676-2L",
    "xc7a75tlfgg484-2L",
    "xc7a75tlcsg324-2L",
    "xc7a100tlcsg324-2L",
    "xc7a100tlfgg484-2L",
    "xc7a100tlfgg676-2L",
    "xc7a100tlftg256-2L",
    "xc7a200tlfbg484-2L",
    "xc7a200tlfbg676-2L",
    "xc7a200tlfbv484-2L",
    "xc7a200tlfbv676-2L",
    "xc7a200tlffg1156-2L",
    "xc7a200tlffv1156-2L",
    "xc7a200tlsbg484-2L",
    "xc7a200tlsbv484-2L",
    "xa7a35tcsg325-1I",
    "xa7a35tcsg325-1Q",
    "xa7a35tcsg325-2I",
    "xa7a35tcsg324-1I",
    "xa7a35tcsg324-1Q",
    "xa7a35tcsg324-2I",
    "xa7a35tcpg236-1I",
    "xa7a35tcpg236-1Q",
    "xa7a35tcpg236-2I",
    "xa7a15tcpg236-1I",
    "xa7a15tcpg236-1Q",
    "xa7a15tcpg236-2I",
    "xa7a15tcsg324-1I",
    "xa7a15tcsg324-1Q",
    "xa7a15tcsg324-2I",
    "xa7a15tcsg325-1I",
    "xa7a15tcsg325-1Q",
    "xa7a15tcsg325-2I",
    "xa7a50tcpg236-1I",
    "xa7a50tcpg236-1Q",
    "xa7a50tcpg236-2I",
    "xa7a50tcsg324-1I",
    "xa7a50tcsg324-1Q",
    "xa7a50tcsg324-2I",
    "xa7a50tcsg325-1I",
    "xa7a50tcsg325-1Q",
    "xa7a50tcsg325-2I",
    "xa7a100tfgg484-1I",
    "xa7a100tfgg484-1Q",
    "xa7a100tfgg484-2I",
    "xa7a100tcsg324-1I",
    "xa7a100tcsg324-1Q",
    "xa7a100tcsg324-2I",
    "xa7a75tcsg324-1I",
    "xa7a75tcsg324-1Q",
    "xa7a75tcsg324-2I",
    "xa7a75tfgg484-1I",
    "xa7a75tfgg484-1Q",
    "xa7a75tfgg484-2I",
    "xa7a12tcpg238-1I",
    "xa7a12tcpg238-1Q",
    "xa7a12tcpg238-2I",
    "xa7a12tcsg325-1I",
    "xa7a12tcsg325-1Q",
    "xa7a12tcsg325-2I",
    "xa7a25tcpg238-1I",
    "xa7a25tcpg238-1Q",
    "xa7a25tcpg238-2I",
    "xa7a25tcsg325-1I",
    "xa7a25tcsg325-1Q",
    "xa7a25tcsg325-2I",
    "xc7z010iclg225-1L",
    "xc7z010iclg400-1L",
    "xc7z010clg400-1",
    "xc7z010clg400-2",
    "xc7z010clg400-3",
    "xc7z010clg225-1",
    "xc7z010clg225-2",
    "xc7z010clg225-3",
    "xc7z007sclg400-1",
    "xc7z007sclg400-2",
    "xc7z007sclg225-1",
    "xc7z007sclg225-2",
    "xc7z015iclg485-1L",
    "xc7z015clg485-1",
    "xc7z015clg485-2",
    "xc7z015clg485-3",
    "xc7z012sclg485-1",
    "xc7z012sclg485-2",
    "xc7z020iclg484-1L",
    "xc7z020iclg400-1L",
    "xc7z014sclg484-1",
    "xc7z014sclg484-2",
    "xc7z014sclg400-1",
    "xc7z014sclg400-2",
    "xc7z020clg484-1",
    "xc7z020clg484-2",
    "xc7z020clg484-3",
    "xc7z020clg400-1",
    "xc7z020clg400-2",
    "xc7z020clg400-3",
    "xc7z030ifbg484-2L",
    "xc7z030ifbg676-2L",
    "xc7z030ifbv484-2L",
    "xc7z030ifbv676-2L",
    "xc7z030iffg676-2L",
    "xc7z030iffv676-2L",
    "xc7z030isbg485-2L",
    "xc7z030isbv485-2L",
    "xc7z030sbg485-1",
    "xc7z030sbg485-2",
    "xc7z030sbg485-3",
    "xc7z030sbv485-1",
    "xc7z030sbv485-2",
    "xc7z030sbv485-3",
    "xc7z030fbg484-1",
    "xc7z030fbg484-2",
    "xc7z030fbg484-3",
    "xc7z030fbg676-1",
    "xc7z030fbg676-2",
    "xc7z030fbg676-3",
    "xc7z030fbv484-1",
    "xc7z030fbv484-2",
    "xc7z030fbv484-3",
    "xc7z030fbv676-1",
    "xc7z030fbv676-2",
    "xc7z030fbv676-3",
    "xc7z030ffg676-1",
    "xc7z030ffg676-2",
    "xc7z030ffg676-3",
    "xc7z030ffv676-1",
    "xc7z030ffv676-2",
    "xc7z030ffv676-3",
    "xa7z010clg225-1I",
    "xa7z010clg225-1Q",
    "xa7z010clg400-1I",
    "xa7z010clg400-1Q",
    "xa7z020clg400-1I",
    "xa7z020clg400-1Q",
    "xa7z020clg484-1I",
    "xa7z020clg484-1Q",
    "xa7z030fbg484-1I",
    "xa7z030fbg484-1Q",
    "xa7z030fbv484-1I",
    "xa7z030fbv484-1Q",
    "xc7s6ftgb196-1",
    "xc7s6ftgb196-1IL",
    "xc7s6ftgb196-1Q",
    "xc7s6ftgb196-2",
    "xc7s6csga225-1",
    "xc7s6csga225-1IL",
    "xc7s6csga225-1Q",
    "xc7s6csga225-2",
    "xc7s6cpga196-1",
    "xc7s6cpga196-1IL",
    "xc7s6cpga196-1Q",
    "xc7s6cpga196-2",
    "xc7s15cpga196-1",
    "xc7s15cpga196-1IL",
    "xc7s15cpga196-1Q",
    "xc7s15cpga196-2",
    "xc7s15csga225-1",
    "xc7s15csga225-1IL",
    "xc7s15csga225-1Q",
    "xc7s15csga225-2",
    "xc7s15ftgb196-1",
    "xc7s15ftgb196-1IL",
    "xc7s15ftgb196-1Q",
    "xc7s15ftgb196-2",
    "xc7s25ftgb196-1",
    "xc7s25ftgb196-1IL",
    "xc7s25ftgb196-1Q",
    "xc7s25ftgb196-2",
    "xc7s25csga324-1",
    "xc7s25csga324-1IL",
    "xc7s25csga324-1Q",
    "xc7s25csga324-2",
    "xc7s25csga225-1",
    "xc7s25csga225-1IL",
    "xc7s25csga225-1Q",
    "xc7s25csga225-2",
    "xc7s50csga324-1",
    "xc7s50csga324-1IL",
    "xc7s50csga324-1Q",
    "xc7s50csga324-2",
    "xc7s50fgga484-1",
    "xc7s50fgga484-1IL",
    "xc7s50fgga484-1Q",
    "xc7s50fgga484-2",
    "xc7s50ftgb196-1",
    "xc7s50ftgb196-1IL",
    "xc7s50ftgb196-1Q",
    "xc7s50ftgb196-2",
    "xc7s100fgga676-1",
    "xc7s100fgga676-1IL",
    "xc7s100fgga676-1Q",
    "xc7s100fgga676-2",
    "xc7s100fgga484-1",
    "xc7s100fgga484-1IL",
    "xc7s100fgga484-1Q",
    "xc7s100fgga484-2",
    "xc7s75fgga484-1",
    "xc7s75fgga484-1IL",
    "xc7s75fgga484-1Q",
    "xc7s75fgga484-2",
    "xc7s75fgga676-1",
    "xc7s75fgga676-1IL",
    "xc7s75fgga676-1Q",
    "xc7s75fgga676-2",
    "xa7s6cpga196-1I",
    "xa7s6cpga196-1Q",
    "xa7s6cpga196-2I",
    "xa7s6csga225-1I",
    "xa7s6csga225-1Q",
    "xa7s6csga225-2I",
    "xa7s6ftgb196-1I",
    "xa7s6ftgb196-1Q",
    "xa7s6ftgb196-2I",
    "xa7s15cpga196-1I",
    "xa7s15cpga196-1Q",
    "xa7s15cpga196-2I",
    "xa7s15csga225-1I",
    "xa7s15csga225-1Q",
    "xa7s15csga225-2I",
    "xa7s15ftgb196-1I",
    "xa7s15ftgb196-1Q",
    "xa7s15ftgb196-2I",
    "xa7s25csga225-1I",
    "xa7s25csga225-1Q",
    "xa7s25csga225-2I",
    "xa7s25csga324-1I",
    "xa7s25csga324-1Q",
    "xa7s25csga324-2I",
    "xa7s25ftgb196-1I",
    "xa7s25ftgb196-1Q",
    "xa7s25ftgb196-2I",
    "xa7s50csga324-1I",
    "xa7s50csga324-1Q",
    "xa7s50csga324-2I",
    "xa7s50fgga484-1I",
    "xa7s50fgga484-1Q",
    "xa7s50fgga484-2I",
    "xa7s50ftgb196-1I",
    "xa7s50ftgb196-1Q",
    "xa7s50ftgb196-2I",
    "xa7s75fgga484-1I",
    "xa7s75fgga484-1Q",
    "xa7s75fgga484-2I",
    "xa7s75fgga676-1I",
    "xa7s75fgga676-1Q",
    "xa7s75fgga676-2I",
    "xa7s100fgga484-1I",
    "xa7s100fgga484-1Q",
    "xa7s100fgga484-2I",
]


def test_start():
    global vivado
    vivado = v.start()
    assert vivado.isalive() == True


def test_get_parts():
    print(v.get_parts())
    assert v.get_parts() == available_parts
