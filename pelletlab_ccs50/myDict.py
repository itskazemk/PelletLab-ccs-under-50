import uuid
from typing import List


class AreaAnalyzeClass:
    def __init__(self, id: uuid.UUID, type: int):
        self.areaAnalyzeID = id
        self.type = type

    def __str__(self):
        return f'id: {self.areaAnalyzeID}, type: {self.type}'


areaAnalyzeIds = {
    'area500_aftermix_moisture_input': AreaAnalyzeClass(uuid.UUID('A5A42908-E381-4B52-A172-585216044695'), 1),
    'area500_beforemix_atomic_k2o': AreaAnalyzeClass(uuid.UUID('C02A7DE2-D0F8-4660-AEF6-3C49504FFE09'), 1),
    'area500_beforemix_atomic_na2o': AreaAnalyzeClass(uuid.UUID('BBBA243B-3874-402D-92AC-C456B7AB942D'), 1),
    'area500_beforemix_blaine_b': AreaAnalyzeClass(uuid.UUID('0249CD4C-FD14-40EC-B24C-968AD61A7AD6'), 1),
    'area500_beforemix_blaine_bs': AreaAnalyzeClass(uuid.UUID('886D4A8F-B889-46DF-8877-15E16F4E1F70'), 1),
    'area500_beforemix_blaine_e': AreaAnalyzeClass(uuid.UUID('682A0F13-E3C5-4C3E-957D-965F11FE4079'), 1),
    'area500_beforemix_blaine_es': AreaAnalyzeClass(uuid.UUID('2401D1F9-E5D5-47A4-9DA7-E04C18CAB252'), 1),
    'area500_beforemix_blaine_p': AreaAnalyzeClass(uuid.UUID('F89C6424-6108-475C-B0D7-2FF577EE269A'), 1),
    'area500_beforemix_blaine_ps': AreaAnalyzeClass(uuid.UUID('A45B98AC-C4F7-456D-B92E-71747F4CD6DC'), 1),
    'area500_beforemix_blaine_result': AreaAnalyzeClass(uuid.UUID('619D6204-32E1-4864-95C3-FF7B8471976F'), 2),
    'area500_beforemix_blaine_ss': AreaAnalyzeClass(uuid.UUID('B5A599F9-3583-49ED-A3DC-4954991E734E'), 1),
    'area500_beforemix_blaine_t': AreaAnalyzeClass(uuid.UUID('52D94368-04BF-4FFD-B4E5-BD128F7CE467'), 1),
    'area500_beforemix_blaine_ts': AreaAnalyzeClass(uuid.UUID('8D5F7CA3-3BF2-4693-96FA-48CB745100E2'), 1),
    'area500_beforemix_feo_avg': AreaAnalyzeClass(uuid.UUID('79E80B6D-248D-4DDB-BBA7-B0C2E6B7AFDF'), 2),
    'area500_beforemix_feo_input1': AreaAnalyzeClass(uuid.UUID('5AC3DE5D-97CC-4225-854D-2A64A1E6DA57'), 1),
    'area500_beforemix_feo_input2': AreaAnalyzeClass(uuid.UUID('4EA14FB5-50A1-4891-A80A-C80A72ED749A'), 1),
    'area500_beforemix_moisture_input': AreaAnalyzeClass(uuid.UUID('D8C12CEC-F09C-45F5-9ECC-16CDF47E54DB'), 1),
    'area500_beforemix_sulfur_input': AreaAnalyzeClass(uuid.UUID('E01CE4AF-7D15-4F36-924C-1AA7BE3BB312'), 1),
    'area500_beforemix_tfe_avg': AreaAnalyzeClass(uuid.UUID('F40C6FA1-7262-4C6E-8D57-DB74E372B597'), 2),
    'area500_beforemix_tfe_input1': AreaAnalyzeClass(uuid.UUID('BAB79868-61DE-4C01-AC67-37EF54695CF7'), 1),
    'area500_beforemix_tfe_input2': AreaAnalyzeClass(uuid.UUID('21174BB9-1F19-4CE5-9F42-6B6A86A95968'), 1),
    'area500_beforemix_xray_al2o3': AreaAnalyzeClass(uuid.UUID('B8DCC36D-DAF4-459D-844F-A6AD2993E898'), 1),
    'area500_beforemix_xray_cao': AreaAnalyzeClass(uuid.UUID('EEA0F384-52E1-46FB-8FDF-DDA42CB80FD0'), 1),
    'area500_beforemix_xray_mgo': AreaAnalyzeClass(uuid.UUID('7CD113B7-0A61-4015-808E-858751C651F4'), 1),
    'area500_beforemix_xray_mno': AreaAnalyzeClass(uuid.UUID('4BB1D94D-01B7-49A1-8591-26F003A8FB70'), 1),
    'area500_beforemix_xray_p': AreaAnalyzeClass(uuid.UUID('774D6D29-879B-400A-8897-BDA2F327D60B'), 1),
    'area500_beforemix_xray_sio2': AreaAnalyzeClass(uuid.UUID('08078DA3-21FD-4ECA-AE6A-78BC28D300A4'), 1),
    'area500_beforemix_xray_tio2': AreaAnalyzeClass(uuid.UUID('C777D50C-0DB2-4253-9740-B3BC75305FE2'), 1),
    'area500_wf1_blaine_b': AreaAnalyzeClass(uuid.UUID('30352BE4-A4C3-4A23-8C7B-400B6735F99A'), 1),
    'area500_wf1_blaine_bs': AreaAnalyzeClass(uuid.UUID('93AEB6F1-2341-4D7A-ACD8-56E22A9076FE'), 1),
    'area500_wf1_blaine_e': AreaAnalyzeClass(uuid.UUID('5ECA91FD-79F5-4380-9260-F536EC76B612'), 1),
    'area500_wf1_blaine_es': AreaAnalyzeClass(uuid.UUID('CDAC7B0B-5B27-492D-A03F-484891232B05'), 1),
    'area500_wf1_blaine_p': AreaAnalyzeClass(uuid.UUID('E64482D3-46F4-40F6-B7F2-AD69B06F1DAB'), 1),
    'area500_wf1_blaine_ps': AreaAnalyzeClass(uuid.UUID('365D1E6D-204D-473A-AEC2-278432EA4B75'), 1),
    'area500_wf1_blaine_result': AreaAnalyzeClass(uuid.UUID('962C02A7-85AC-494F-B5C0-18758A809C51'), 2),
    'area500_wf1_blaine_ss': AreaAnalyzeClass(uuid.UUID('9BB41220-4449-49E7-BC30-A98DF912A419'), 1),
    'area500_wf1_blaine_t': AreaAnalyzeClass(uuid.UUID('1A3AA509-39E1-4A84-9AAB-42B66CA3FDD4'), 1),
    'area500_wf1_blaine_ts': AreaAnalyzeClass(uuid.UUID('211FB2E6-FC0C-4F94-A918-4F55E6FE27E6'), 1),
    'area500_wf1_feo_avg': AreaAnalyzeClass(uuid.UUID('A6C1666C-CD68-4496-A53F-3B07769BA6E7'), 2),
    'area500_wf1_feo_input1': AreaAnalyzeClass(uuid.UUID('F8F1925E-2A91-4B3A-A648-8850613ECC98'), 1),
    'area500_wf1_feo_input2': AreaAnalyzeClass(uuid.UUID('A8D2F1C4-A88F-4BE5-BB77-D9D209DD439E'), 1),
    'area500_wf1_moisture_input': AreaAnalyzeClass(uuid.UUID('5B66DB57-0F58-44F5-8796-CBECDD60D7E5'), 1),
    'area500_wf1_tfe_avg': AreaAnalyzeClass(uuid.UUID('3E38D705-3923-4DF2-BB6A-80CEBE33E412'), 2),
    'area500_wf1_tfe_input1': AreaAnalyzeClass(uuid.UUID('82ECA41B-C4BF-44FA-A91E-8FEF1A50AA71'), 1),
    'area500_wf1_tfe_input2': AreaAnalyzeClass(uuid.UUID('DB62A0AF-53A6-4E2E-895C-AB66C161F3CA'), 1),
    'area500_wf10_moisture_input': AreaAnalyzeClass(uuid.UUID('0A3CB80D-EED5-48E6-BB03-DE2C1252AFD8'), 1),
    'area500_wf2_blaine_b': AreaAnalyzeClass(uuid.UUID('1ED7ABD5-AB47-4BDF-974B-EA4CF2A29749'), 1),
    'area500_wf2_blaine_bs': AreaAnalyzeClass(uuid.UUID('50450BF6-2283-426A-9120-A515FA18F3A1'), 1),
    'area500_wf2_blaine_e': AreaAnalyzeClass(uuid.UUID('5A4B7EDF-EBBE-45CD-B2C7-C555CECECE62'), 1),
    'area500_wf2_blaine_es': AreaAnalyzeClass(uuid.UUID('7204A770-0A60-4132-BA6B-CBC7E1E424F1'), 1),
    'area500_wf2_blaine_p': AreaAnalyzeClass(uuid.UUID('E30D904C-EE81-44FB-8BA2-153F381E3B98'), 1),
    'area500_wf2_blaine_ps': AreaAnalyzeClass(uuid.UUID('97BF62AE-19FB-4955-9146-2C51323E31DC'), 1),
    'area500_wf2_blaine_result': AreaAnalyzeClass(uuid.UUID('FE8BF0E7-F56A-4A3A-B2CF-20268CB66D24'), 2),
    'area500_wf2_blaine_ss': AreaAnalyzeClass(uuid.UUID('55A99244-8A6E-46BF-B194-6CDC66180572'), 1),
    'area500_wf2_blaine_t': AreaAnalyzeClass(uuid.UUID('F60BA2F9-D679-4116-B0F2-C563B5961515'), 1),
    'area500_wf2_blaine_ts': AreaAnalyzeClass(uuid.UUID('90BA2485-F5D2-4460-97EE-401D65E17D5B'), 1),
    'area500_wf2_feo_avg': AreaAnalyzeClass(uuid.UUID('E3CABFE4-A494-464F-A242-332212E1D2EF'), 2),
    'area500_wf2_feo_input1': AreaAnalyzeClass(uuid.UUID('B47B53E1-9686-423B-9488-E3A714DD12AB'), 1),
    'area500_wf2_feo_input2': AreaAnalyzeClass(uuid.UUID('B690BFB0-6D8B-49A8-A2DF-8C4CA5D04A96'), 1),
    'area500_wf2_moisture_input': AreaAnalyzeClass(uuid.UUID('A0D8D26F-2E61-422B-947E-DD8E15375EE8'), 1),
    'area500_wf2_tfe_avg': AreaAnalyzeClass(uuid.UUID('0C3E8A6D-987C-4CEF-B07B-43E175FBDB8A'), 2),
    'area500_wf2_tfe_input1': AreaAnalyzeClass(uuid.UUID('A572CB4D-A662-4977-9402-E19E6FC9E63A'), 1),
    'area500_wf2_tfe_input2': AreaAnalyzeClass(uuid.UUID('8877A4EF-B3A7-4293-9387-4DB50AAF7A09'), 1),
    'area500_wf3_blaine_b': AreaAnalyzeClass(uuid.UUID('2CB35812-A305-44FF-8DA8-C6D8B0BADDA8'), 1),
    'area500_wf3_blaine_bs': AreaAnalyzeClass(uuid.UUID('A0E1FF85-CDBA-41C0-88AC-42667F00F344'), 1),
    'area500_wf3_blaine_e': AreaAnalyzeClass(uuid.UUID('B2CB5FE3-41FC-4F94-830B-DB10CEDF543B'), 1),
    'area500_wf3_blaine_es': AreaAnalyzeClass(uuid.UUID('123E9E92-0649-45B3-A2AD-D801E31ED8B6'), 1),
    'area500_wf3_blaine_p': AreaAnalyzeClass(uuid.UUID('4118518E-8519-4EF1-844A-3DD2542EEBA0'), 1),
    'area500_wf3_blaine_ps': AreaAnalyzeClass(uuid.UUID('812C9DE5-ED76-48F4-8541-E90A94AFBD6A'), 1),
    'area500_wf3_blaine_result': AreaAnalyzeClass(uuid.UUID('60E8C7D6-D71D-40FE-9A26-88302CFB9BEF'), 2),
    'area500_wf3_blaine_ss': AreaAnalyzeClass(uuid.UUID('AF325AEA-7D37-41B2-8654-B154CBE2FB72'), 1),
    'area500_wf3_blaine_t': AreaAnalyzeClass(uuid.UUID('5CBB40A5-80C9-4E4E-BCE4-AF46B0D52271'), 1),
    'area500_wf3_blaine_ts': AreaAnalyzeClass(uuid.UUID('6D403D5A-584B-48F3-BFF8-8BFD1C823030'), 1),
    'area500_wf3_feo_avg': AreaAnalyzeClass(uuid.UUID('52AA46A1-9D07-4581-BC08-9E7CAF24494E'), 2),
    'area500_wf3_feo_input1': AreaAnalyzeClass(uuid.UUID('A851476F-C371-4010-AF2B-6A9862E0D02B'), 1),
    'area500_wf3_feo_input2': AreaAnalyzeClass(uuid.UUID('8AF560DC-9017-45ED-BFF0-B4BE06A815E8'), 1),
    'area500_wf3_moisture_input': AreaAnalyzeClass(uuid.UUID('13AC627F-1CD1-4AFA-8B86-B2F93EDE165B'), 1),
    'area500_wf3_tfe_avg': AreaAnalyzeClass(uuid.UUID('301DD985-194F-42FC-8513-1DC23EAD22A3'), 2),
    'area500_wf3_tfe_input1': AreaAnalyzeClass(uuid.UUID('150C0240-4E59-42CE-BFDD-F42D309842D3'), 1),
    'area500_wf3_tfe_input2': AreaAnalyzeClass(uuid.UUID('39FD3F5B-2909-4D17-A469-917B643C7667'), 1),
    'area500_wf4_blaine_b': AreaAnalyzeClass(uuid.UUID('83BDAA19-CFFF-4CB4-906A-55DF9B2245AB'), 1),
    'area500_wf4_blaine_bs': AreaAnalyzeClass(uuid.UUID('77BE2260-13A1-4515-B6A2-D1E87DFF15BD'), 1),
    'area500_wf4_blaine_e': AreaAnalyzeClass(uuid.UUID('79FD70DE-2452-484B-9C3A-7F79E90C2ED6'), 1),
    'area500_wf4_blaine_es': AreaAnalyzeClass(uuid.UUID('2CEA40D1-C51C-4349-BE0B-B1580DDAF779'), 1),
    'area500_wf4_blaine_p': AreaAnalyzeClass(uuid.UUID('2C629EE9-CE73-4762-AA46-82D1010A1C40'), 1),
    'area500_wf4_blaine_ps': AreaAnalyzeClass(uuid.UUID('59AE9FE2-F546-42B5-81DE-8A8D74259652'), 1),
    'area500_wf4_blaine_result': AreaAnalyzeClass(uuid.UUID('43D30779-590F-4DDB-AFF5-85AF5EA62F3A'), 2),
    'area500_wf4_blaine_ss': AreaAnalyzeClass(uuid.UUID('41E689D6-CF17-4FEE-B14A-3ED9B92E6EBA'), 1),
    'area500_wf4_blaine_t': AreaAnalyzeClass(uuid.UUID('2658C69A-AED7-483D-991B-43CDE8D9FEC7'), 1),
    'area500_wf4_blaine_ts': AreaAnalyzeClass(uuid.UUID('D6043C09-AF63-4FCB-8075-118584EE6E27'), 1),
    'area500_wf4_feo_avg': AreaAnalyzeClass(uuid.UUID('84C72310-6C25-4700-A172-94EEFDEA39D4'), 2),
    'area500_wf4_feo_input1': AreaAnalyzeClass(uuid.UUID('265911B9-E0D0-44C5-8EE5-5738CDF77FEA'), 1),
    'area500_wf4_feo_input2': AreaAnalyzeClass(uuid.UUID('A3D8730A-019E-4771-9107-947B528DEA3D'), 1),
    'area500_wf4_moisture_input': AreaAnalyzeClass(uuid.UUID('9D9AA284-DDBF-4573-AD36-59976BDFA014'), 1),
    'area500_wf4_tfe_avg': AreaAnalyzeClass(uuid.UUID('A3E89171-A0B6-4F93-AC4A-3DD0A148BF03'), 2),
    'area500_wf4_tfe_input1': AreaAnalyzeClass(uuid.UUID('DD4A8E2C-3455-4581-AB9C-D50D278EE581'), 1),
    'area500_wf4_tfe_input2': AreaAnalyzeClass(uuid.UUID('D02C010C-249F-4344-BA38-7EA651ED8EA7'), 1),
    'area500_wf5_blaine_b': AreaAnalyzeClass(uuid.UUID('7C6442FA-F99F-4C7B-9C47-17CFC92D8E54'), 1),
    'area500_wf5_blaine_bs': AreaAnalyzeClass(uuid.UUID('09E940A6-82BF-4BA5-9B02-730E48B7BDFE'), 1),
    'area500_wf5_blaine_e': AreaAnalyzeClass(uuid.UUID('5B5AD798-3663-4D8F-AEAA-E095AA26A966'), 1),
    'area500_wf5_blaine_es': AreaAnalyzeClass(uuid.UUID('BF872D53-459D-4BF7-8122-0EE99C317659'), 1),
    'area500_wf5_blaine_p': AreaAnalyzeClass(uuid.UUID('45189832-59B0-4284-B1ED-C5BB33F8E241'), 1),
    'area500_wf5_blaine_ps': AreaAnalyzeClass(uuid.UUID('E967DEBD-F4F2-419E-AA53-8AE772358D7F'), 1),
    'area500_wf5_blaine_result': AreaAnalyzeClass(uuid.UUID('AB81938C-6F18-4297-9ACF-726C4754F301'), 2),
    'area500_wf5_blaine_ss': AreaAnalyzeClass(uuid.UUID('C2203CA1-6971-4430-8BF7-90FCAD2128AC'), 1),
    'area500_wf5_blaine_t': AreaAnalyzeClass(uuid.UUID('6A7A38EC-ADB9-4872-8441-F7F21B52D0CB'), 1),
    'area500_wf5_blaine_ts': AreaAnalyzeClass(uuid.UUID('5F417E7F-C4B4-4777-A18A-B8C22AAA9D67'), 1),
    'area500_wf5_feo_avg': AreaAnalyzeClass(uuid.UUID('8257D37F-343D-4A02-864F-ECAAFC119846'), 2),
    'area500_wf5_feo_input1': AreaAnalyzeClass(uuid.UUID('D90654E4-458D-4D1C-81B8-0DDA4F6E37CC'), 1),
    'area500_wf5_feo_input2': AreaAnalyzeClass(uuid.UUID('44DBA22D-CC0D-4F66-BA24-7DEB2CC6DFB4'), 1),
    'area500_wf5_moisture_input': AreaAnalyzeClass(uuid.UUID('813478E0-775A-4B33-B2E8-2C9910FE7374'), 1),
    'area500_wf5_tfe_avg': AreaAnalyzeClass(uuid.UUID('AA4A3032-DDB8-42A6-86B6-FE5E210BD434'), 2),
    'area500_wf5_tfe_input1': AreaAnalyzeClass(uuid.UUID('EB3FCC54-03B1-44CC-9E40-FD0CBAEE391C'), 1),
    'area500_wf5_tfe_input2': AreaAnalyzeClass(uuid.UUID('F9176D07-F485-41D8-900A-07CE7B410D13'), 1),
    'area500_wf6_blaine_b': AreaAnalyzeClass(uuid.UUID('EACCFA12-1197-4D30-827D-10EA8821C8FC'), 1),
    'area500_wf6_blaine_bs': AreaAnalyzeClass(uuid.UUID('9BCF9AB5-3E2C-4F9A-B934-004BEB55E9E6'), 1),
    'area500_wf6_blaine_e': AreaAnalyzeClass(uuid.UUID('D2CE54B4-569C-4705-A661-FC43EADF8D43'), 1),
    'area500_wf6_blaine_es': AreaAnalyzeClass(uuid.UUID('F208A2D7-AA1F-46AC-9550-F7B85F5D8067'), 1),
    'area500_wf6_blaine_p': AreaAnalyzeClass(uuid.UUID('7807A2B7-77F5-44C7-8E60-16D57D204CAF'), 1),
    'area500_wf6_blaine_ps': AreaAnalyzeClass(uuid.UUID('B63B4E5C-7F54-42FE-8DA1-FA09630168C9'), 1),
    'area500_wf6_blaine_result': AreaAnalyzeClass(uuid.UUID('623A0B63-B09F-4C10-B986-8AD91FDA1ED2'), 2),
    'area500_wf6_blaine_ss': AreaAnalyzeClass(uuid.UUID('F1FA5ED8-DB8C-4D0A-B03B-16AB3937095A'), 1),
    'area500_wf6_blaine_t': AreaAnalyzeClass(uuid.UUID('00161B92-F182-4BEF-AB34-5CF829E76453'), 1),
    'area500_wf6_blaine_ts': AreaAnalyzeClass(uuid.UUID('18943E7E-A79C-4B32-A216-02272ABBA0B2'), 1),
    'area500_wf6_feo_avg': AreaAnalyzeClass(uuid.UUID('BA6AA62B-FAA5-4CD4-BB33-3DB82A2B10B4'), 2),
    'area500_wf6_feo_input1': AreaAnalyzeClass(uuid.UUID('BC6C5EAE-3634-440B-A78C-070D5A2E5F50'), 1),
    'area500_wf6_feo_input2': AreaAnalyzeClass(uuid.UUID('80A3663E-C2B1-4A73-8A21-5E95E92DA4D4'), 1),
    'area500_wf6_moisture_input': AreaAnalyzeClass(uuid.UUID('61788DFE-2D22-4D78-98F8-198F7F6E60CB'), 1),
    'area500_wf6_tfe_avg': AreaAnalyzeClass(uuid.UUID('A34EF638-D8F4-43F4-A4C9-60F40F338108'), 2),
    'area500_wf6_tfe_input1': AreaAnalyzeClass(uuid.UUID('FB48D801-A4D8-47D6-9A0D-1BD4D6CCDE04'), 1),
    'area500_wf6_tfe_input2': AreaAnalyzeClass(uuid.UUID('61212A42-F4D0-4E25-9252-FC50E819787E'), 1),
    'area500_wf7_moisture_input': AreaAnalyzeClass(uuid.UUID('53A1D56B-0D67-4DA7-9A69-56C37A7E60E3'), 1),
    'area500_wf8_moisture_input': AreaAnalyzeClass(uuid.UUID('4F22ED5B-AD51-416C-98CE-8274C1E9D088'), 1),
    'area500_wf9_moisture_input': AreaAnalyzeClass(uuid.UUID('74B598BA-ADF6-4888-A2F4-4CF3A0397674'), 1),
}

areaAnalyzeIdToName = {v.areaAnalyzeID: k for k, v in areaAnalyzeIds.items()}

getAttrHtmName = {

    # 'beforemix_xrays': '',
    'aftermix_moisture510bc1s': 'area500_aftermix_moisture_input',
    'beforemix_moisture500s': 'area500_beforemix_moisture_input',
    'beforemix_tfes': 'area500_beforemix_tfe_avg',
    'beforemix_feos': 'area500_beforemix_feo_avg',
    'beforemix_sulfors': 'area500_beforemix_sulfur_input',
    'beforemix_belines': 'area500_beforemix_blaine_result',
    'wf1_feos': 'area500_wf1_feo_avg',
    'wf2_feos': 'area500_wf2_feo_avg',
    'wf3_feos': 'area500_wf3_feo_avg',
    'wf4_feos': 'area500_wf4_feo_avg',
    'wf5_feos': 'area500_wf5_feo_avg',
    'wf6_feos': 'area500_wf6_feo_avg',
    'wf7_feos': 'area500_wf7_feo_avg',
    'wf8_feos': 'area500_wf8_feo_avg',
    'wf9_feos': 'area500_wf9_feo_avg',
    'wf10_feos': 'area500_wf10_feo_avg',
    'wf1_moistures': 'area500_wf1_moisture_input',
    'wf2_moistures': 'area500_wf2_moisture_input',
    'wf3_moistures': 'area500_wf3_moisture_input',
    'wf4_moistures': 'area500_wf4_moisture_input',
    'wf5_moistures': 'area500_wf5_moisture_input',
    'wf6_moistures': 'area500_wf6_moisture_input',
    'wf7_moistures': 'area500_wf7_moisture_input',
    'wf8_moistures': 'area500_wf8_moisture_input',
    'wf9_moistures': 'area500_wf9_moisture_input',
    'wf10_moistures': 'area500_wf10_moisture_input',
    'wf1_belines': 'area500_wf1_blaine_result',
    'wf2_belines': 'area500_wf2_blaine_result',
    'wf3_belines': 'area500_wf3_blaine_result',
    'wf4_belines': 'area500_wf4_blaine_result',
    'wf5_belines': 'area500_wf5_blaine_result',
    'wf6_belines': 'area500_wf6_blaine_result',
    'wf7_belines': 'area500_wf7_blaine_result',
    'wf8_belines': 'area500_wf8_blaine_result',
    'wf9_belines': 'area500_wf9_blaine_result',
    'wf10_belines': 'area500_wf10_blaine_result',
    'wf1_tfes': 'area500_wf1_tfe_avg',
    'wf2_tfes': 'area500_wf2_tfe_avg',
    'wf3_tfes': 'area500_wf3_tfe_avg',
    'wf4_tfes': 'area500_wf4_tfe_avg',
    'wf5_tfes': 'area500_wf5_tfe_avg',
    'wf6_tfes': 'area500_wf6_tfe_avg',
    'wf7_tfes': 'area500_wf7_tfe_avg',
    'wf8_tfes': 'area500_wf8_tfe_avg',
    'wf9_tfes': 'area500_wf9_tfe_avg',
    'wf10_tfes': 'area500_wf10_tfe_avg',
}


class ValueListClass:
    def __init__(self):
        self.area500_aftermix_moisture_input = []
        self.area500_beforemix_moisture_input = []
        self.area500_beforemix_blaine_result = []
        self.area500_beforemix_xray_sio2 = []
        self.area500_beforemix_xray_cao = []
        self.area500_beforemix_xray_mgo = []
        self.area500_beforemix_xray_al2o3 = []
        self.area500_beforemix_xray_p = []
        self.area500_beforemix_xray_mno = []
        self.area500_beforemix_xray_tio2 = []
        self.area500_beforemix_tfe_avg = []
        self.area500_beforemix_feo_avg = []
        self.area500_wf1_moisture_input = []
        self.area500_wf2_moisture_input = []
        self.area500_wf3_moisture_input = []
        self.area500_wf4_moisture_input = []
        self.area500_wf5_moisture_input = []
        self.area500_wf6_moisture_input = []
        self.area500_wf7_moisture_input = []
        self.area500_wf8_moisture_input = []
        self.area500_wf9_moisture_input = []
        self.area500_wf10_moisture_input = []
        self.area500_wf1_blaine_result = []
        self.area500_wf2_blaine_result = []
        self.area500_wf3_blaine_result = []
        self.area500_wf4_blaine_result = []
        self.area500_wf5_blaine_result = []
        self.area500_wf6_blaine_result = []
        self.area500_wf7_blaine_result = []
        self.area500_wf8_blaine_result = []
        self.area500_wf9_blaine_result = []
        self.area500_wf10_blaine_result = []
        self.area500_wf1_tfe_avg = []
        self.area500_wf2_tfe_avg = []
        self.area500_wf3_tfe_avg = []
        self.area500_wf4_tfe_avg = []
        self.area500_wf5_tfe_avg = []
        self.area500_wf6_tfe_avg = []
        self.area500_wf7_tfe_avg = []
        self.area500_wf8_tfe_avg = []
        self.area500_wf9_tfe_avg = []
        self.area500_wf10_tfe_avg = []
        self.area500_wf1_feo_avg = []
        self.area500_wf2_feo_avg = []
        self.area500_wf3_feo_avg = []
        self.area500_wf4_feo_avg = []
        self.area500_wf5_feo_avg = []
        self.area500_wf6_feo_avg = []
        self.area500_wf7_feo_avg = []
        self.area500_wf8_feo_avg = []
        self.area500_wf9_feo_avg = []
        self.area500_wf10_feo_avg = []

    def __repr__(self):
        message = ''
        for name, value in self.__dict__.items():
            if value and isinstance(value, list):
                message += f'len({name})={len(value)} '
        return message if message else 'Empty'

    def __iter__(self):
        for attribute_name, value in self.__dict__.items():
            if value and isinstance(value, list):
                yield attribute_name, value

            # if isinstance(value, list):
            #     yield attribute_name, value

    def has_any_list_with_value(self):
        pass
        # return any(value for value in self.__dict__.values() if value)
