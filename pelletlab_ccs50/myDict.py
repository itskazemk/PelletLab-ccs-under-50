import uuid
from typing import List


class AreaAnalyzeClass:
    def __init__(self, id: uuid.UUID, type: int):
        self.areaAnalyzeID = id
        self.type = type

    def __str__(self):
        return f"id: {self.areaAnalyzeID}, type: {self.type}"


areaAnalyzeIds = {
    "area110_110_20micron_passing": AreaAnalyzeClass(
        uuid.UUID("30E87BED-88C2-4306-85E0-C6CA7CBA97F6"), 2
    ),
    "area110_110_20micron_wa": AreaAnalyzeClass(
        uuid.UUID("0038A7A1-4DC2-41CC-9DAB-4186CE901977"), 1
    ),
    "area110_110_20micron_wb": AreaAnalyzeClass(
        uuid.UUID("5412728C-3954-4E8D-A67A-B07DCAE6ECC1"), 1
    ),
    "area110_110_20micron_ws": AreaAnalyzeClass(
        uuid.UUID("00FE8D5D-4299-4793-9190-2BEA8B850420"), 1
    ),
    "area110_110_25micron_passing": AreaAnalyzeClass(
        uuid.UUID("17213468-FB45-4641-9A28-8B7962967ECD"), 2
    ),
    "area110_110_25micron_wa": AreaAnalyzeClass(
        uuid.UUID("6E0B3E4E-6848-4CCA-AF5B-C83DF6A772B6"), 1
    ),
    "area110_110_25micron_wb": AreaAnalyzeClass(
        uuid.UUID("E0646EE6-E246-40D4-BFE5-487656A301F9"), 1
    ),
    "area110_110_25micron_ws": AreaAnalyzeClass(
        uuid.UUID("032AFDCE-180A-449D-8153-C689C3006A8D"), 1
    ),
    "area110_110_45micron_passing": AreaAnalyzeClass(
        uuid.UUID("544CC563-39A8-46F6-9136-D3E0F114E3DF"), 2
    ),
    "area110_110_45micron_wa": AreaAnalyzeClass(
        uuid.UUID("9171F975-8D89-4241-BE3D-A2657E0A6F9B"), 1
    ),
    "area110_110_45micron_wb": AreaAnalyzeClass(
        uuid.UUID("97BCCD16-146F-4E38-BFF9-2D296AF34FBA"), 1
    ),
    "area110_110_45micron_ws": AreaAnalyzeClass(
        uuid.UUID("049294CE-9AEF-42D2-BA51-DE8A69F0C125"), 1
    ),
    "area110_110_atomic_k2o": AreaAnalyzeClass(
        uuid.UUID("1B3E8030-E486-4313-B0ED-6504463B11B7"), 1
    ),
    "area110_110_atomic_na2o": AreaAnalyzeClass(
        uuid.UUID("300E6632-25F6-449D-853C-0F523F0B20E2"), 1
    ),
    "area110_110_blaine_b": AreaAnalyzeClass(
        uuid.UUID("D894D75D-FAE4-4D82-ABB9-6763B823E2CB"), 1
    ),
    "area110_110_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("1117972C-6505-48FC-A027-6EDE6117E8FF"), 1
    ),
    "area110_110_blaine_e": AreaAnalyzeClass(
        uuid.UUID("D10FB0FF-1D29-4302-9762-CF19F24F7B10"), 1
    ),
    "area110_110_blaine_es": AreaAnalyzeClass(
        uuid.UUID("EB317343-78E6-47C5-85DB-524D3F7CE9A0"), 1
    ),
    "area110_110_blaine_p": AreaAnalyzeClass(
        uuid.UUID("7D9676A6-E86F-4BD9-B222-ADAD99363B83"), 1
    ),
    "area110_110_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("53415646-CC41-4C26-B029-83ED4CD443B8"), 1
    ),
    "area110_110_blaine_result": AreaAnalyzeClass(
        uuid.UUID("9E2408BE-409B-4FA6-96BE-ED3C7F05CACE"), 2
    ),
    "area110_110_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("81D995EB-203E-40C6-9C08-02D428545EDF"), 1
    ),
    "area110_110_blaine_t": AreaAnalyzeClass(
        uuid.UUID("22C63354-40B3-47A4-BC02-6868C0209DBA"), 1
    ),
    "area110_110_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("6B2A4AF7-5A28-4808-BD1E-359BB8215167"), 1
    ),
    "area110_110_description_input1": AreaAnalyzeClass(
        uuid.UUID("326E275E-4657-4311-866D-892073640D1F"), 1
    ),
    "area110_110_feo_avg": AreaAnalyzeClass(
        uuid.UUID("D0E22008-DBC1-4C16-8F5C-5A2F7EAB777D"), 2
    ),
    "area110_110_feo_input1": AreaAnalyzeClass(
        uuid.UUID("D14285A5-87EE-4D6E-87E7-54654BFFA5E2"), 1
    ),
    "area110_110_feo_input2": AreaAnalyzeClass(
        uuid.UUID("3A4462B3-6AB1-45E0-99EF-BA502A9888AA"), 1
    ),
    "area110_110_moisture_input": AreaAnalyzeClass(
        uuid.UUID("24358176-A9FC-49E9-B894-E0D62180AAD2"), 1
    ),
    "area110_110_sulfur_input": AreaAnalyzeClass(
        uuid.UUID("FBB9E276-F781-4617-A2D4-DE26AB2904F0"), 1
    ),
    "area110_110_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("5CB278A7-B3A1-4813-B6DB-56D52149330C"), 2
    ),
    "area110_110_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("3232C272-6D9D-427E-8365-58E28561DAE8"), 1
    ),
    "area110_110_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("D292EDE8-BD4F-4FC4-A4F4-AC6B6F8A23E8"), 1
    ),
    "area110_110_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("DB4ADE58-DCD7-4FEB-BAF6-9518B775855E"), 1
    ),
    "area110_110_xray_cao": AreaAnalyzeClass(
        uuid.UUID("1B95D14B-97F1-40AF-AA9D-AB78E14D4205"), 1
    ),
    "area110_110_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("2AC18D52-172C-481E-841F-2FAE15E798CA"), 1
    ),
    "area110_110_xray_mno": AreaAnalyzeClass(
        uuid.UUID("769B9586-5E3D-4191-877D-B444F9CEE763"), 1
    ),
    "area110_110_xray_p": AreaAnalyzeClass(
        uuid.UUID("EAA98594-E210-406A-ACC9-11C714E08A12"), 1
    ),
    "area110_110_xray_result": AreaAnalyzeClass(
        uuid.UUID("B4C3A72F-7180-4FB4-8E83-99FA8185DA46"), 2
    ),
    "area110_110_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("B7E4BB83-CAB9-4E3F-8844-A6DBE99D7B30"), 1
    ),
    "area110_110_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("F7787804-8A45-4DD3-AD5B-1C3E9EE58619"), 1
    ),
    "area150_afterhpgr_20micron_passing": AreaAnalyzeClass(
        uuid.UUID("C82366E2-E433-4D65-93D6-9024B78F7D7F"), 2
    ),
    "area150_afterhpgr_20micron_wa": AreaAnalyzeClass(
        uuid.UUID("7AC83E5A-918D-4B7C-838C-947263AA6C01"), 1
    ),
    "area150_afterhpgr_20micron_wb": AreaAnalyzeClass(
        uuid.UUID("5C55671E-A3BF-457A-8AEE-CDD3A952E7F5"), 1
    ),
    "area150_afterhpgr_20micron_ws": AreaAnalyzeClass(
        uuid.UUID("A54A7D03-2353-45B5-B973-526718F32816"), 1
    ),
    "area150_afterhpgr_25micron_passing": AreaAnalyzeClass(
        uuid.UUID("538316E7-A1E9-496B-B704-114787F0CFF7"), 2
    ),
    "area150_afterhpgr_25micron_wa": AreaAnalyzeClass(
        uuid.UUID("40929CA8-3465-4D34-807F-5FBC69AD55EE"), 1
    ),
    "area150_afterhpgr_25micron_wb": AreaAnalyzeClass(
        uuid.UUID("A967CFC9-FCCA-41C9-83FF-0D704ABB6E36"), 1
    ),
    "area150_afterhpgr_25micron_ws": AreaAnalyzeClass(
        uuid.UUID("56F0B093-17B4-4949-AE61-634B1271D2D2"), 1
    ),
    "area150_afterhpgr_45micron_passing": AreaAnalyzeClass(
        uuid.UUID("7D7823C4-D2A3-42DC-83A8-BDD133619BD3"), 2
    ),
    "area150_afterhpgr_45micron_wa": AreaAnalyzeClass(
        uuid.UUID("65BB3626-AC57-4E92-8C49-498E9CCCCD5F"), 1
    ),
    "area150_afterhpgr_45micron_wb": AreaAnalyzeClass(
        uuid.UUID("63601F0E-B6A7-4156-9607-95654CD8741F"), 1
    ),
    "area150_afterhpgr_45micron_ws": AreaAnalyzeClass(
        uuid.UUID("4C95D076-766A-4FE9-B627-54BC0626E65E"), 1
    ),
    "area150_afterhpgr_blaine_b": AreaAnalyzeClass(
        uuid.UUID("8B4D0FED-1E46-4292-9E2B-EC6E736DFC84"), 1
    ),
    "area150_afterhpgr_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("6C5E3BED-4A8D-448E-86D7-42B221D1FD72"), 1
    ),
    "area150_afterhpgr_blaine_e": AreaAnalyzeClass(
        uuid.UUID("C4EA7714-BA3D-466D-B8FE-4743D37C21FC"), 1
    ),
    "area150_afterhpgr_blaine_es": AreaAnalyzeClass(
        uuid.UUID("7036D1FC-D0D2-447A-A46A-7E07D083F7BA"), 1
    ),
    "area150_afterhpgr_blaine_p": AreaAnalyzeClass(
        uuid.UUID("8A991B90-8F97-4F16-9BDF-79FAF24E0E59"), 1
    ),
    "area150_afterhpgr_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("0EA90CD7-FBF6-4668-B72F-02EA84A9657E"), 1
    ),
    "area150_afterhpgr_blaine_result": AreaAnalyzeClass(
        uuid.UUID("954A7CB7-E883-4BFB-A91F-27253006EDA8"), 2
    ),
    "area150_afterhpgr_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("4158EF77-BAE9-4682-8B8E-0F6E618F2653"), 1
    ),
    "area150_afterhpgr_blaine_t": AreaAnalyzeClass(
        uuid.UUID("07F522AB-A4ED-41BF-8255-792082C2F419"), 1
    ),
    "area150_afterhpgr_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("ED1C526F-F9EA-4B6E-85B3-DDD93F888A14"), 1
    ),
    "area150_afterhpgr_moisture_input": AreaAnalyzeClass(
        uuid.UUID("E74D9B37-CF61-424F-B512-6F97280BD211"), 1
    ),
    "area150_beforehpgr_20micron_passing": AreaAnalyzeClass(
        uuid.UUID("EBDC4491-4AE6-47AA-9373-A627379B9722"), 2
    ),
    "area150_beforehpgr_20micron_wa": AreaAnalyzeClass(
        uuid.UUID("0A90EA2F-572D-48C1-B185-1BCDA0FBFA3B"), 1
    ),
    "area150_beforehpgr_20micron_wb": AreaAnalyzeClass(
        uuid.UUID("10603A0D-0C64-4C7E-92FB-388451ECF170"), 1
    ),
    "area150_beforehpgr_20micron_ws": AreaAnalyzeClass(
        uuid.UUID("27D04B0F-7705-4904-97FE-D8C50B014FBB"), 1
    ),
    "area150_beforehpgr_25micron_passing": AreaAnalyzeClass(
        uuid.UUID("96E2A170-C913-4347-AF66-B5CA53463C66"), 2
    ),
    "area150_beforehpgr_25micron_wa": AreaAnalyzeClass(
        uuid.UUID("33A99EDE-2431-4119-AB4F-82493404BC6E"), 1
    ),
    "area150_beforehpgr_25micron_wb": AreaAnalyzeClass(
        uuid.UUID("619F6E31-8CB3-429A-87E7-DD146DE8EEB6"), 1
    ),
    "area150_beforehpgr_25micron_ws": AreaAnalyzeClass(
        uuid.UUID("6C085D72-7547-4C0A-AE4C-1F17B2948589"), 1
    ),
    "area150_beforehpgr_45micron_passing": AreaAnalyzeClass(
        uuid.UUID("390A6B45-50B9-4DA1-8A88-08EBF37CE087"), 2
    ),
    "area150_beforehpgr_45micron_wa": AreaAnalyzeClass(
        uuid.UUID("5D057D7C-6502-4E0E-8810-0EB80D676DA0"), 1
    ),
    "area150_beforehpgr_45micron_wb": AreaAnalyzeClass(
        uuid.UUID("AE5FED33-7AEF-4D9F-93F4-1EF65DEA9A99"), 1
    ),
    "area150_beforehpgr_45micron_ws": AreaAnalyzeClass(
        uuid.UUID("8CA07A77-798C-4060-ACA8-1AF44C58B9B7"), 1
    ),
    "area150_beforehpgr_blaine_b": AreaAnalyzeClass(
        uuid.UUID("89423C2E-BFB0-4A36-97C7-5F74710B1C3C"), 1
    ),
    "area150_beforehpgr_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("2239A76A-6951-45DB-AD8D-E2AB9CD42A49"), 1
    ),
    "area150_beforehpgr_blaine_e": AreaAnalyzeClass(
        uuid.UUID("64CD7854-B069-4987-BB49-7C5634730E1F"), 1
    ),
    "area150_beforehpgr_blaine_es": AreaAnalyzeClass(
        uuid.UUID("9A9E9186-010A-4B21-ABDB-42BD594D3F32"), 1
    ),
    "area150_beforehpgr_blaine_p": AreaAnalyzeClass(
        uuid.UUID("EF824DD9-D84D-4C1B-B06F-B87876935068"), 1
    ),
    "area150_beforehpgr_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("20AB6A2D-952B-4F96-9E70-EADD0E6C0AD7"), 1
    ),
    "area150_beforehpgr_blaine_result": AreaAnalyzeClass(
        uuid.UUID("5CB109F5-AD3A-4133-92AF-B155AFCB5E1A"), 2
    ),
    "area150_beforehpgr_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("5225DC66-6211-43D2-9D40-AB81CE39195E"), 1
    ),
    "area150_beforehpgr_blaine_t": AreaAnalyzeClass(
        uuid.UUID("11E874BE-A564-43C7-9AE6-79CEDE03B48E"), 1
    ),
    "area150_beforehpgr_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("AD015274-3B69-4608-A145-B63141CF279E"), 1
    ),
    "area150_beforehpgr_moisture_input": AreaAnalyzeClass(
        uuid.UUID("AD9BCC0A-5AEA-4EC8-9B2C-972B0138889F"), 1
    ),
    "area160_160_20micron_passing": AreaAnalyzeClass(
        uuid.UUID("2DD4CBF2-491D-47F0-94AF-BD93E069AE9A"), 2
    ),
    "area160_160_20micron_wa": AreaAnalyzeClass(
        uuid.UUID("83F1E942-5BD0-4F70-92D9-8B865C2B57A0"), 1
    ),
    "area160_160_20micron_wb": AreaAnalyzeClass(
        uuid.UUID("6CE7DD01-36AE-4D9C-BEA3-1F8047E10718"), 1
    ),
    "area160_160_20micron_ws": AreaAnalyzeClass(
        uuid.UUID("7C06C53E-02F5-41E7-99D5-C0C371AD815D"), 1
    ),
    "area160_160_25micron_passing": AreaAnalyzeClass(
        uuid.UUID("AEFF2F07-8310-410A-B27E-22A4902C9E82"), 2
    ),
    "area160_160_25micron_wa": AreaAnalyzeClass(
        uuid.UUID("85310872-4F3A-4EC4-80EB-DFF80B38C736"), 1
    ),
    "area160_160_25micron_wb": AreaAnalyzeClass(
        uuid.UUID("AFC4142F-188B-411D-8BDF-410365FC9251"), 1
    ),
    "area160_160_25micron_ws": AreaAnalyzeClass(
        uuid.UUID("98A8460B-E5B0-44F0-836F-44C032AF421F"), 1
    ),
    "area160_160_45micron_passing": AreaAnalyzeClass(
        uuid.UUID("DE0863AB-8BC7-4750-B0B6-29D585175882"), 2
    ),
    "area160_160_45micron_wa": AreaAnalyzeClass(
        uuid.UUID("658E8EB6-DCC0-41D8-9ED4-E0BE9DD28C1D"), 1
    ),
    "area160_160_45micron_wb": AreaAnalyzeClass(
        uuid.UUID("5329F692-40BC-433B-8906-BBB39E2A6D26"), 1
    ),
    "area160_160_45micron_ws": AreaAnalyzeClass(
        uuid.UUID("77B15CEC-56A9-4045-9E78-6B8993926D88"), 1
    ),
    "area160_160_atomic_k2o": AreaAnalyzeClass(
        uuid.UUID("42A92AC2-A334-4CC7-A683-C753D5C2E2AD"), 1
    ),
    "area160_160_atomic_na2o": AreaAnalyzeClass(
        uuid.UUID("85CA1E3F-F68B-416D-A77D-C6B2383C7122"), 1
    ),
    "area160_160_blaine_b": AreaAnalyzeClass(
        uuid.UUID("A92177E7-77A6-4FD5-B9D0-5DC0BADBB16A"), 1
    ),
    "area160_160_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("94D979F3-AC48-43FA-8F34-6E0CFF5A4C2B"), 1
    ),
    "area160_160_blaine_e": AreaAnalyzeClass(
        uuid.UUID("E516D093-DD31-498C-8D68-0D3B41DD03C8"), 1
    ),
    "area160_160_blaine_es": AreaAnalyzeClass(
        uuid.UUID("D986DFBB-2A7B-4676-B76C-978403F25042"), 1
    ),
    "area160_160_blaine_p": AreaAnalyzeClass(
        uuid.UUID("9A50A349-F13A-4087-85FD-435477018214"), 1
    ),
    "area160_160_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("27FD00A1-BA18-4444-A154-704FC6F844E9"), 1
    ),
    "area160_160_blaine_result": AreaAnalyzeClass(
        uuid.UUID("18511BC1-E3D7-4246-8C41-B28295048A05"), 2
    ),
    "area160_160_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("A5E1D92E-4390-4CDB-8EE0-199A41D984B7"), 1
    ),
    "area160_160_blaine_t": AreaAnalyzeClass(
        uuid.UUID("B7F06F4D-8C0B-4138-AEDE-B82C4845EB0F"), 1
    ),
    "area160_160_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("A59091DC-AE62-4DC4-A054-2CB9A459043D"), 1
    ),
    "area160_160_feo_avg": AreaAnalyzeClass(
        uuid.UUID("2904217F-71B6-468A-86FF-D32620156F2F"), 2
    ),
    "area160_160_feo_input1": AreaAnalyzeClass(
        uuid.UUID("65B2CE9B-1CD0-4A3B-8612-C6658D6C35D8"), 1
    ),
    "area160_160_feo_input2": AreaAnalyzeClass(
        uuid.UUID("75E22D1A-7EF2-4E9F-A5F6-31CED5DF3821"), 1
    ),
    "area160_160_moisture_input": AreaAnalyzeClass(
        uuid.UUID("6CB4C2EE-B2C7-4F04-9F9B-6CB3DAEAEDFA"), 1
    ),
    "area160_160_sulfur_input": AreaAnalyzeClass(
        uuid.UUID("31EF2600-EBBD-4AC5-84CE-6ECF85A113EE"), 1
    ),
    "area160_160_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("7B967A25-3D3C-4EAD-8EF6-42A064A7A1BB"), 2
    ),
    "area160_160_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("B9823EA9-E720-4386-8F09-3355514AE649"), 1
    ),
    "area160_160_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("51D64831-EDD0-4194-A3D7-E0C582E84722"), 1
    ),
    "area160_160_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("E365BDB1-1312-4A40-9FBE-22343725E0CB"), 1
    ),
    "area160_160_xray_cao": AreaAnalyzeClass(
        uuid.UUID("F8EEA092-B12D-4354-8E53-E740C8264CAE"), 1
    ),
    "area160_160_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("1F133C9D-2B6F-408F-9148-AF70A30BFEDD"), 1
    ),
    "area160_160_xray_mno": AreaAnalyzeClass(
        uuid.UUID("13E07DD0-FBC0-4F49-BDF3-D2EC947BBC34"), 1
    ),
    "area160_160_xray_p": AreaAnalyzeClass(
        uuid.UUID("50952FD6-C35B-42EF-B9F5-C004F82B3800"), 1
    ),
    "area160_160_xray_result": AreaAnalyzeClass(
        uuid.UUID("E08370CD-6044-47DE-AC73-267D309C7FB8"), 2
    ),
    "area160_160_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("ABBC34E4-0152-443A-9439-F94A8B22287F"), 1
    ),
    "area160_160_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("949904C8-0801-40D7-88D4-41B46A83EFDB"), 1
    ),
    "area210_210cc1_45micron_passing": AreaAnalyzeClass(
        uuid.UUID("26A8D273-7ACF-45EC-A17B-8EC64C90EBC8"), 2
    ),
    "area210_210cc1_45micron_wa": AreaAnalyzeClass(
        uuid.UUID("9DC0B959-C634-4CD1-89A4-4D281BADCF43"), 1
    ),
    "area210_210cc1_45micron_wb": AreaAnalyzeClass(
        uuid.UUID("F69E5DF4-E273-4218-B367-AB6940F4F6EB"), 1
    ),
    "area210_210cc1_45micron_ws": AreaAnalyzeClass(
        uuid.UUID("511484C2-B438-4C35-924E-985F06E117E2"), 1
    ),
    "area210_210cc1_cao_input": AreaAnalyzeClass(
        uuid.UUID("67B27F2C-C600-4240-9986-3CCB5C2C75A0"), 2
    ),
    "area210_210cc1_loi_input": AreaAnalyzeClass(
        uuid.UUID("03CFFD67-D0DF-4567-A010-E8BED1E31574"), 2
    ),
    "area210_210cc1_mgo_input": AreaAnalyzeClass(
        uuid.UUID("B8443801-995A-476A-9E67-DF86A82C728B"), 2
    ),
    "area210_210cc1_moisture_input": AreaAnalyzeClass(
        uuid.UUID("E40EEB34-4D8B-489A-AC06-673385999E2E"), 1
    ),
    "area210_210cc1_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("75C72E41-DA18-4882-985A-8C76612A260B"), 1
    ),
    "area210_210cc1_xray_cao": AreaAnalyzeClass(
        uuid.UUID("CC78534E-09F3-42BB-BBC3-E818AEB943F3"), 1
    ),
    "area210_210cc1_xray_fe": AreaAnalyzeClass(
        uuid.UUID("3F25CF28-BD94-4136-87FC-6411070666D9"), 1
    ),
    "area210_210cc1_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("21BDAF4D-DBC8-4A63-997C-750C9B4A72A8"), 1
    ),
    "area210_210cc1_xray_mno": AreaAnalyzeClass(
        uuid.UUID("A0891577-447B-4172-8460-C64154124D12"), 1
    ),
    "area210_210cc1_xray_p": AreaAnalyzeClass(
        uuid.UUID("30C531D6-BD0D-4751-A667-3B8B80D0A2F5"), 1
    ),
    "area210_210cc1_xray_result": AreaAnalyzeClass(
        uuid.UUID("BA84CF67-9013-4FE4-919C-E62A8BDED896"), 2
    ),
    "area210_210cc1_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("4E4A2021-921A-4933-AFE4-4090FF10FAF4"), 1
    ),
    "area210_210cc1_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("5865B833-3D53-4CC1-86EC-E778A5E3311C"), 1
    ),
    "area210_210wf1_cao_input": AreaAnalyzeClass(
        uuid.UUID("561AE03D-BF98-4501-9DF3-3DDF21FC9DCD"), 2
    ),
    "area210_210wf1_loi_input": AreaAnalyzeClass(
        uuid.UUID("ECFD9D02-B813-4AD5-AED0-41A44A31FE91"), 2
    ),
    "area210_210wf1_mgo_input": AreaAnalyzeClass(
        uuid.UUID("6701523E-583E-4153-9E16-0CEC0079A82F"), 2
    ),
    "area210_210wf1_moisture_input": AreaAnalyzeClass(
        uuid.UUID("9F6E4457-FD50-4749-B66F-051BA754DA92"), 1
    ),
    "area210_210wf1_sievesize_1625mm": AreaAnalyzeClass(
        uuid.UUID("66CAF333-8274-4883-A198-888C497CCD4A"), 1
    ),
    "area210_210wf1_sievesize_1625w": AreaAnalyzeClass(
        uuid.UUID("D4762CDF-7DB5-40E3-98F7-DD494AF17009"), 1
    ),
    "area210_210wf1_sievesize_25mm": AreaAnalyzeClass(
        uuid.UUID("11CF944D-5D41-45DE-BBBF-989EE3AB5CD8"), 1
    ),
    "area210_210wf1_sievesize_25w": AreaAnalyzeClass(
        uuid.UUID("E68AABCA-1562-40F1-BDDD-74D7C2C1174D"), 1
    ),
    "area210_210wf1_sievesize_33563mm": AreaAnalyzeClass(
        uuid.UUID("67138717-CD62-4627-99D2-3ECA8DC36876"), 1
    ),
    "area210_210wf1_sievesize_33563w": AreaAnalyzeClass(
        uuid.UUID("7E4766F7-42E6-435E-B31E-606FEEAC6E56"), 1
    ),
    "area210_210wf1_sievesize_335w": AreaAnalyzeClass(
        uuid.UUID("85A49F3A-36A1-47CD-A067-8E369DDF482D"), 1
    ),
    "area210_210wf1_sievesize_35mm": AreaAnalyzeClass(
        uuid.UUID("4238AA6F-F8E5-49A2-901A-8CD94BE49BD9"), 1
    ),
    "area210_210wf1_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("DF151912-A4BC-46C8-98AF-7E79AFB4F2E3"), 1
    ),
    "area210_210wf1_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("39963CA4-12D7-4DEC-9082-E9CB4CC5D3ED"), 2
    ),
    "area210_210wf1_sievesize_916mm": AreaAnalyzeClass(
        uuid.UUID("2ADF7021-E043-475B-B706-7B1995800CF3"), 1
    ),
    "area210_210wf1_sievesize_916w": AreaAnalyzeClass(
        uuid.UUID("2E385602-FAB7-4BDB-845B-3EA603DA82B5"), 1
    ),
    "area210_210wf1_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("D9568AEE-362D-41A7-B04D-977FF5B8791E"), 1
    ),
    "area210_210wf1_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("C5A84264-37C2-40FE-8594-57F4EE282D1A"), 1
    ),
    "area210_210wf1_xray_cao": AreaAnalyzeClass(
        uuid.UUID("465D026D-3A6A-4A5F-89E7-2E29511AEA3C"), 1
    ),
    "area210_210wf1_xray_fe": AreaAnalyzeClass(
        uuid.UUID("4F01DD2A-4B82-478F-AC31-5E734959AB6A"), 1
    ),
    "area210_210wf1_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("1D5AF14B-BFC6-49ED-AE2D-6B0E13A51B11"), 1
    ),
    "area210_210wf1_xray_mno": AreaAnalyzeClass(
        uuid.UUID("63334FFD-4ADF-4DBA-8E42-F32A029867F1"), 1
    ),
    "area210_210wf1_xray_p": AreaAnalyzeClass(
        uuid.UUID("686B0140-CA02-43E6-B53F-6194D0980E05"), 1
    ),
    "area210_210wf1_xray_result": AreaAnalyzeClass(
        uuid.UUID("EA326E51-9FEA-4F90-987A-874AFD1A5A38"), 2
    ),
    "area210_210wf1_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("1D08E4B8-132C-4698-B3C8-DF7EE826D6EE"), 1
    ),
    "area210_210wf1_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("0AE7F7D8-D093-4B98-BB4D-B1017D95A721"), 1
    ),
    "area310_310_45micron_passing": AreaAnalyzeClass(
        uuid.UUID("438E4672-5052-43C9-9B51-99F165E4E1F4"), 2
    ),
    "area310_310_45micron_wa": AreaAnalyzeClass(
        uuid.UUID("740CA807-D796-4F27-AA56-0609B04093D6"), 1
    ),
    "area310_310_45micron_wb": AreaAnalyzeClass(
        uuid.UUID("92B47ACF-C9DA-4405-AABF-C0F515599B1F"), 1
    ),
    "area310_310_45micron_ws": AreaAnalyzeClass(
        uuid.UUID("4A50F117-3FC4-48B4-B55E-F78F4103F975"), 1
    ),
    "area310_310_moisture_input": AreaAnalyzeClass(
        uuid.UUID("C342DC0E-5626-4865-B9D7-23C44D911513"), 1
    ),
    "area310_310_waterabsorption_k": AreaAnalyzeClass(
        uuid.UUID("4E58ED4F-CA1A-4DA7-AFBD-FF72B32CB994"), 1
    ),
    "area310_310_waterabsorption_result": AreaAnalyzeClass(
        uuid.UUID("3237C877-A06F-45D3-83AC-E3D245DBA813"), 1
    ),
    "area310_310_waterabsorption_t1": AreaAnalyzeClass(
        uuid.UUID("FA3B198B-08A5-4BFF-A5F6-B9FE6777237E"), 1
    ),
    "area310_310_waterabsorption_t2": AreaAnalyzeClass(
        uuid.UUID("00573CEE-A55D-43B2-B1E0-17D4A3BFBBD1"), 1
    ),
    "area310_310_waterabsorption_tr": AreaAnalyzeClass(
        uuid.UUID("3841B392-98EC-44C6-BFC3-F28E9BEB91FD"), 1
    ),
    "area310_310_waterabsorption_w0": AreaAnalyzeClass(
        uuid.UUID("BD4D41EA-E281-4963-90E8-75FAFBBF5BB3"), 1
    ),
    "area310_310_waterabsorption_w1": AreaAnalyzeClass(
        uuid.UUID("F48DA14F-D0DB-4EA6-926C-A60C91964885"), 1
    ),
    "area310_310_waterabsorption_w2": AreaAnalyzeClass(
        uuid.UUID("F61BF9CA-EC10-4B8C-BAC3-E5E4B81FB5D4"), 1
    ),
    "area310_310_waterabsorption2_k": AreaAnalyzeClass(
        uuid.UUID("27568AAF-A4D5-4492-9D92-51B63D1BD34C"), 1
    ),
    "area310_310_waterabsorption2_result": AreaAnalyzeClass(
        uuid.UUID("18FBFAD3-49A8-49A7-AA04-36784BC2AE12"), 2
    ),
    "area310_310_waterabsorption2_t1": AreaAnalyzeClass(
        uuid.UUID("A3886709-8A91-469F-AF36-721B355D11A7"), 1
    ),
    "area310_310_waterabsorption2_t2": AreaAnalyzeClass(
        uuid.UUID("41181CFE-E5FE-471A-8614-53B5AA633E72"), 1
    ),
    "area310_310_waterabsorption2_tr": AreaAnalyzeClass(
        uuid.UUID("5D131212-8F7C-4FB0-9865-29EB7E2EE45C"), 1
    ),
    "area310_310_waterabsorption2_w0": AreaAnalyzeClass(
        uuid.UUID("D888F531-3C76-41FE-8095-741DB2E0813C"), 1
    ),
    "area310_310_waterabsorption2_w1": AreaAnalyzeClass(
        uuid.UUID("16FC7F24-12B7-4B63-851D-AD318DFFC6C4"), 1
    ),
    "area310_310_waterabsorption2_w2": AreaAnalyzeClass(
        uuid.UUID("985DE21C-A5DE-4909-B3E3-7FC46750AE97"), 1
    ),
    "area310_310_waterabsorption3_k": AreaAnalyzeClass(
        uuid.UUID("7D35673E-2BED-4351-918F-85C6BB4BFCFB"), 1
    ),
    "area310_310_waterabsorption3_result": AreaAnalyzeClass(
        uuid.UUID("1273F8B6-C93A-4FEC-8327-8CF444EF0772"), 2
    ),
    "area310_310_waterabsorption3_t1": AreaAnalyzeClass(
        uuid.UUID("97E0E275-847C-479F-A42A-BBACC9E33755"), 1
    ),
    "area310_310_waterabsorption3_t2": AreaAnalyzeClass(
        uuid.UUID("DAFCCF0C-85C5-4740-900B-DA7500BD6520"), 1
    ),
    "area310_310_waterabsorption3_tr": AreaAnalyzeClass(
        uuid.UUID("FE22F532-0571-4251-86ED-2013A6CA34F6"), 1
    ),
    "area310_310_waterabsorption3_w0": AreaAnalyzeClass(
        uuid.UUID("2BC93B3C-18E5-4F0E-8A42-837BFBDF532C"), 1
    ),
    "area310_310_waterabsorption3_w1": AreaAnalyzeClass(
        uuid.UUID("0EC39E57-8C1B-4108-837B-31B8D0263B67"), 1
    ),
    "area310_310_waterabsorption3_w2": AreaAnalyzeClass(
        uuid.UUID("85A678E8-D11D-405F-905A-A732213CDCEB"), 1
    ),
    "area310_310_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("8FD6BC7C-6C7E-4DFC-AA46-639A6C7272AF"), 1
    ),
    "area310_310_xray_cao": AreaAnalyzeClass(
        uuid.UUID("1BD0AFAD-25EA-44F4-9672-05109F81E97E"), 1
    ),
    "area310_310_xray_fe": AreaAnalyzeClass(
        uuid.UUID("6F732F2A-7712-46FA-BCD4-18715E920862"), 1
    ),
    "area310_310_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("E222D1C5-0BFF-45C7-AE7F-F02418CE2CA2"), 1
    ),
    "area310_310_xray_mno": AreaAnalyzeClass(
        uuid.UUID("26E329BA-E260-4618-8463-A0A2F8DC52A6"), 1
    ),
    "area310_310_xray_p": AreaAnalyzeClass(
        uuid.UUID("C369E0F4-CA2C-4767-BABF-E843E8C134B0"), 1
    ),
    "area310_310_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("E78A4535-F16B-4D26-BA99-0A4FF284C8C5"), 1
    ),
    "area310_310_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("BEEA3FD6-95EF-4A13-9339-71A12D3D401D"), 1
    ),
    "area500_aftermix_moisture_input": AreaAnalyzeClass(
        uuid.UUID("A5A42908-E381-4B52-A172-585216044695"), 1
    ),
    "area500_beforemix_atomic_k2o": AreaAnalyzeClass(
        uuid.UUID("C02A7DE2-D0F8-4660-AEF6-3C49504FFE09"), 1
    ),
    "area500_beforemix_atomic_na2o": AreaAnalyzeClass(
        uuid.UUID("BBBA243B-3874-402D-92AC-C456B7AB942D"), 1
    ),
    "area500_beforemix_blaine_b": AreaAnalyzeClass(
        uuid.UUID("0249CD4C-FD14-40EC-B24C-968AD61A7AD6"), 1
    ),
    "area500_beforemix_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("886D4A8F-B889-46DF-8877-15E16F4E1F70"), 1
    ),
    "area500_beforemix_blaine_e": AreaAnalyzeClass(
        uuid.UUID("682A0F13-E3C5-4C3E-957D-965F11FE4079"), 1
    ),
    "area500_beforemix_blaine_es": AreaAnalyzeClass(
        uuid.UUID("2401D1F9-E5D5-47A4-9DA7-E04C18CAB252"), 1
    ),
    "area500_beforemix_blaine_p": AreaAnalyzeClass(
        uuid.UUID("F89C6424-6108-475C-B0D7-2FF577EE269A"), 1
    ),
    "area500_beforemix_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("A45B98AC-C4F7-456D-B92E-71747F4CD6DC"), 1
    ),
    "area500_beforemix_blaine_result": AreaAnalyzeClass(
        uuid.UUID("619D6204-32E1-4864-95C3-FF7B8471976F"), 2
    ),
    "area500_beforemix_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("B5A599F9-3583-49ED-A3DC-4954991E734E"), 1
    ),
    "area500_beforemix_blaine_t": AreaAnalyzeClass(
        uuid.UUID("52D94368-04BF-4FFD-B4E5-BD128F7CE467"), 1
    ),
    "area500_beforemix_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("8D5F7CA3-3BF2-4693-96FA-48CB745100E2"), 1
    ),
    "area500_beforemix_feo_avg": AreaAnalyzeClass(
        uuid.UUID("79E80B6D-248D-4DDB-BBA7-B0C2E6B7AFDF"), 2
    ),
    "area500_beforemix_feo_input1": AreaAnalyzeClass(
        uuid.UUID("5AC3DE5D-97CC-4225-854D-2A64A1E6DA57"), 1
    ),
    "area500_beforemix_feo_input2": AreaAnalyzeClass(
        uuid.UUID("4EA14FB5-50A1-4891-A80A-C80A72ED749A"), 1
    ),
    "area500_beforemix_moisture_input": AreaAnalyzeClass(
        uuid.UUID("D8C12CEC-F09C-45F5-9ECC-16CDF47E54DB"), 1
    ),
    "area500_beforemix_sulfur_input": AreaAnalyzeClass(
        uuid.UUID("E01CE4AF-7D15-4F36-924C-1AA7BE3BB312"), 1
    ),
    "area500_beforemix_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("F40C6FA1-7262-4C6E-8D57-DB74E372B597"), 2
    ),
    "area500_beforemix_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("BAB79868-61DE-4C01-AC67-37EF54695CF7"), 1
    ),
    "area500_beforemix_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("21174BB9-1F19-4CE5-9F42-6B6A86A95968"), 1
    ),
    "area500_beforemix_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("B8DCC36D-DAF4-459D-844F-A6AD2993E898"), 1
    ),
    "area500_beforemix_xray_cao": AreaAnalyzeClass(
        uuid.UUID("EEA0F384-52E1-46FB-8FDF-DDA42CB80FD0"), 1
    ),
    "area500_beforemix_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("7CD113B7-0A61-4015-808E-858751C651F4"), 1
    ),
    "area500_beforemix_xray_mno": AreaAnalyzeClass(
        uuid.UUID("4BB1D94D-01B7-49A1-8591-26F003A8FB70"), 1
    ),
    "area500_beforemix_xray_p": AreaAnalyzeClass(
        uuid.UUID("774D6D29-879B-400A-8897-BDA2F327D60B"), 1
    ),
    "area500_beforemix_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("08078DA3-21FD-4ECA-AE6A-78BC28D300A4"), 1
    ),
    "area500_beforemix_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("C777D50C-0DB2-4253-9740-B3BC75305FE2"), 1
    ),
    "area500_wf1_blaine_b": AreaAnalyzeClass(
        uuid.UUID("30352BE4-A4C3-4A23-8C7B-400B6735F99A"), 1
    ),
    "area500_wf1_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("93AEB6F1-2341-4D7A-ACD8-56E22A9076FE"), 1
    ),
    "area500_wf1_blaine_e": AreaAnalyzeClass(
        uuid.UUID("5ECA91FD-79F5-4380-9260-F536EC76B612"), 1
    ),
    "area500_wf1_blaine_es": AreaAnalyzeClass(
        uuid.UUID("CDAC7B0B-5B27-492D-A03F-484891232B05"), 1
    ),
    "area500_wf1_blaine_p": AreaAnalyzeClass(
        uuid.UUID("E64482D3-46F4-40F6-B7F2-AD69B06F1DAB"), 1
    ),
    "area500_wf1_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("365D1E6D-204D-473A-AEC2-278432EA4B75"), 1
    ),
    "area500_wf1_blaine_result": AreaAnalyzeClass(
        uuid.UUID("962C02A7-85AC-494F-B5C0-18758A809C51"), 2
    ),
    "area500_wf1_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("9BB41220-4449-49E7-BC30-A98DF912A419"), 1
    ),
    "area500_wf1_blaine_t": AreaAnalyzeClass(
        uuid.UUID("1A3AA509-39E1-4A84-9AAB-42B66CA3FDD4"), 1
    ),
    "area500_wf1_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("211FB2E6-FC0C-4F94-A918-4F55E6FE27E6"), 1
    ),
    "area500_wf1_feo_avg": AreaAnalyzeClass(
        uuid.UUID("A6C1666C-CD68-4496-A53F-3B07769BA6E7"), 2
    ),
    "area500_wf1_feo_input1": AreaAnalyzeClass(
        uuid.UUID("F8F1925E-2A91-4B3A-A648-8850613ECC98"), 1
    ),
    "area500_wf1_feo_input2": AreaAnalyzeClass(
        uuid.UUID("A8D2F1C4-A88F-4BE5-BB77-D9D209DD439E"), 1
    ),
    "area500_wf1_moisture_input": AreaAnalyzeClass(
        uuid.UUID("5B66DB57-0F58-44F5-8796-CBECDD60D7E5"), 1
    ),
    "area500_wf1_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("3E38D705-3923-4DF2-BB6A-80CEBE33E412"), 2
    ),
    "area500_wf1_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("82ECA41B-C4BF-44FA-A91E-8FEF1A50AA71"), 1
    ),
    "area500_wf1_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("DB62A0AF-53A6-4E2E-895C-AB66C161F3CA"), 1
    ),
    "area500_wf10_moisture_input": AreaAnalyzeClass(
        uuid.UUID("0A3CB80D-EED5-48E6-BB03-DE2C1252AFD8"), 1
    ),
    "area500_wf2_blaine_b": AreaAnalyzeClass(
        uuid.UUID("1ED7ABD5-AB47-4BDF-974B-EA4CF2A29749"), 1
    ),
    "area500_wf2_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("50450BF6-2283-426A-9120-A515FA18F3A1"), 1
    ),
    "area500_wf2_blaine_e": AreaAnalyzeClass(
        uuid.UUID("5A4B7EDF-EBBE-45CD-B2C7-C555CECECE62"), 1
    ),
    "area500_wf2_blaine_es": AreaAnalyzeClass(
        uuid.UUID("7204A770-0A60-4132-BA6B-CBC7E1E424F1"), 1
    ),
    "area500_wf2_blaine_p": AreaAnalyzeClass(
        uuid.UUID("E30D904C-EE81-44FB-8BA2-153F381E3B98"), 1
    ),
    "area500_wf2_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("97BF62AE-19FB-4955-9146-2C51323E31DC"), 1
    ),
    "area500_wf2_blaine_result": AreaAnalyzeClass(
        uuid.UUID("FE8BF0E7-F56A-4A3A-B2CF-20268CB66D24"), 2
    ),
    "area500_wf2_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("55A99244-8A6E-46BF-B194-6CDC66180572"), 1
    ),
    "area500_wf2_blaine_t": AreaAnalyzeClass(
        uuid.UUID("F60BA2F9-D679-4116-B0F2-C563B5961515"), 1
    ),
    "area500_wf2_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("90BA2485-F5D2-4460-97EE-401D65E17D5B"), 1
    ),
    "area500_wf2_feo_avg": AreaAnalyzeClass(
        uuid.UUID("E3CABFE4-A494-464F-A242-332212E1D2EF"), 2
    ),
    "area500_wf2_feo_input1": AreaAnalyzeClass(
        uuid.UUID("B47B53E1-9686-423B-9488-E3A714DD12AB"), 1
    ),
    "area500_wf2_feo_input2": AreaAnalyzeClass(
        uuid.UUID("B690BFB0-6D8B-49A8-A2DF-8C4CA5D04A96"), 1
    ),
    "area500_wf2_moisture_input": AreaAnalyzeClass(
        uuid.UUID("A0D8D26F-2E61-422B-947E-DD8E15375EE8"), 1
    ),
    "area500_wf2_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("0C3E8A6D-987C-4CEF-B07B-43E175FBDB8A"), 2
    ),
    "area500_wf2_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("A572CB4D-A662-4977-9402-E19E6FC9E63A"), 1
    ),
    "area500_wf2_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("8877A4EF-B3A7-4293-9387-4DB50AAF7A09"), 1
    ),
    "area500_wf3_blaine_b": AreaAnalyzeClass(
        uuid.UUID("2CB35812-A305-44FF-8DA8-C6D8B0BADDA8"), 1
    ),
    "area500_wf3_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("A0E1FF85-CDBA-41C0-88AC-42667F00F344"), 1
    ),
    "area500_wf3_blaine_e": AreaAnalyzeClass(
        uuid.UUID("B2CB5FE3-41FC-4F94-830B-DB10CEDF543B"), 1
    ),
    "area500_wf3_blaine_es": AreaAnalyzeClass(
        uuid.UUID("123E9E92-0649-45B3-A2AD-D801E31ED8B6"), 1
    ),
    "area500_wf3_blaine_p": AreaAnalyzeClass(
        uuid.UUID("4118518E-8519-4EF1-844A-3DD2542EEBA0"), 1
    ),
    "area500_wf3_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("812C9DE5-ED76-48F4-8541-E90A94AFBD6A"), 1
    ),
    "area500_wf3_blaine_result": AreaAnalyzeClass(
        uuid.UUID("60E8C7D6-D71D-40FE-9A26-88302CFB9BEF"), 2
    ),
    "area500_wf3_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("AF325AEA-7D37-41B2-8654-B154CBE2FB72"), 1
    ),
    "area500_wf3_blaine_t": AreaAnalyzeClass(
        uuid.UUID("5CBB40A5-80C9-4E4E-BCE4-AF46B0D52271"), 1
    ),
    "area500_wf3_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("6D403D5A-584B-48F3-BFF8-8BFD1C823030"), 1
    ),
    "area500_wf3_feo_avg": AreaAnalyzeClass(
        uuid.UUID("52AA46A1-9D07-4581-BC08-9E7CAF24494E"), 2
    ),
    "area500_wf3_feo_input1": AreaAnalyzeClass(
        uuid.UUID("A851476F-C371-4010-AF2B-6A9862E0D02B"), 1
    ),
    "area500_wf3_feo_input2": AreaAnalyzeClass(
        uuid.UUID("8AF560DC-9017-45ED-BFF0-B4BE06A815E8"), 1
    ),
    "area500_wf3_moisture_input": AreaAnalyzeClass(
        uuid.UUID("13AC627F-1CD1-4AFA-8B86-B2F93EDE165B"), 1
    ),
    "area500_wf3_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("301DD985-194F-42FC-8513-1DC23EAD22A3"), 2
    ),
    "area500_wf3_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("150C0240-4E59-42CE-BFDD-F42D309842D3"), 1
    ),
    "area500_wf3_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("39FD3F5B-2909-4D17-A469-917B643C7667"), 1
    ),
    "area500_wf4_blaine_b": AreaAnalyzeClass(
        uuid.UUID("83BDAA19-CFFF-4CB4-906A-55DF9B2245AB"), 1
    ),
    "area500_wf4_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("77BE2260-13A1-4515-B6A2-D1E87DFF15BD"), 1
    ),
    "area500_wf4_blaine_e": AreaAnalyzeClass(
        uuid.UUID("79FD70DE-2452-484B-9C3A-7F79E90C2ED6"), 1
    ),
    "area500_wf4_blaine_es": AreaAnalyzeClass(
        uuid.UUID("2CEA40D1-C51C-4349-BE0B-B1580DDAF779"), 1
    ),
    "area500_wf4_blaine_p": AreaAnalyzeClass(
        uuid.UUID("2C629EE9-CE73-4762-AA46-82D1010A1C40"), 1
    ),
    "area500_wf4_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("59AE9FE2-F546-42B5-81DE-8A8D74259652"), 1
    ),
    "area500_wf4_blaine_result": AreaAnalyzeClass(
        uuid.UUID("43D30779-590F-4DDB-AFF5-85AF5EA62F3A"), 2
    ),
    "area500_wf4_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("41E689D6-CF17-4FEE-B14A-3ED9B92E6EBA"), 1
    ),
    "area500_wf4_blaine_t": AreaAnalyzeClass(
        uuid.UUID("2658C69A-AED7-483D-991B-43CDE8D9FEC7"), 1
    ),
    "area500_wf4_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("D6043C09-AF63-4FCB-8075-118584EE6E27"), 1
    ),
    "area500_wf4_feo_avg": AreaAnalyzeClass(
        uuid.UUID("84C72310-6C25-4700-A172-94EEFDEA39D4"), 2
    ),
    "area500_wf4_feo_input1": AreaAnalyzeClass(
        uuid.UUID("265911B9-E0D0-44C5-8EE5-5738CDF77FEA"), 1
    ),
    "area500_wf4_feo_input2": AreaAnalyzeClass(
        uuid.UUID("A3D8730A-019E-4771-9107-947B528DEA3D"), 1
    ),
    "area500_wf4_moisture_input": AreaAnalyzeClass(
        uuid.UUID("9D9AA284-DDBF-4573-AD36-59976BDFA014"), 1
    ),
    "area500_wf4_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("A3E89171-A0B6-4F93-AC4A-3DD0A148BF03"), 2
    ),
    "area500_wf4_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("DD4A8E2C-3455-4581-AB9C-D50D278EE581"), 1
    ),
    "area500_wf4_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("D02C010C-249F-4344-BA38-7EA651ED8EA7"), 1
    ),
    "area500_wf5_blaine_b": AreaAnalyzeClass(
        uuid.UUID("7C6442FA-F99F-4C7B-9C47-17CFC92D8E54"), 1
    ),
    "area500_wf5_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("09E940A6-82BF-4BA5-9B02-730E48B7BDFE"), 1
    ),
    "area500_wf5_blaine_e": AreaAnalyzeClass(
        uuid.UUID("5B5AD798-3663-4D8F-AEAA-E095AA26A966"), 1
    ),
    "area500_wf5_blaine_es": AreaAnalyzeClass(
        uuid.UUID("BF872D53-459D-4BF7-8122-0EE99C317659"), 1
    ),
    "area500_wf5_blaine_p": AreaAnalyzeClass(
        uuid.UUID("45189832-59B0-4284-B1ED-C5BB33F8E241"), 1
    ),
    "area500_wf5_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("E967DEBD-F4F2-419E-AA53-8AE772358D7F"), 1
    ),
    "area500_wf5_blaine_result": AreaAnalyzeClass(
        uuid.UUID("AB81938C-6F18-4297-9ACF-726C4754F301"), 2
    ),
    "area500_wf5_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("C2203CA1-6971-4430-8BF7-90FCAD2128AC"), 1
    ),
    "area500_wf5_blaine_t": AreaAnalyzeClass(
        uuid.UUID("6A7A38EC-ADB9-4872-8441-F7F21B52D0CB"), 1
    ),
    "area500_wf5_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("5F417E7F-C4B4-4777-A18A-B8C22AAA9D67"), 1
    ),
    "area500_wf5_feo_avg": AreaAnalyzeClass(
        uuid.UUID("8257D37F-343D-4A02-864F-ECAAFC119846"), 2
    ),
    "area500_wf5_feo_input1": AreaAnalyzeClass(
        uuid.UUID("D90654E4-458D-4D1C-81B8-0DDA4F6E37CC"), 1
    ),
    "area500_wf5_feo_input2": AreaAnalyzeClass(
        uuid.UUID("44DBA22D-CC0D-4F66-BA24-7DEB2CC6DFB4"), 1
    ),
    "area500_wf5_moisture_input": AreaAnalyzeClass(
        uuid.UUID("813478E0-775A-4B33-B2E8-2C9910FE7374"), 1
    ),
    "area500_wf5_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("AA4A3032-DDB8-42A6-86B6-FE5E210BD434"), 2
    ),
    "area500_wf5_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("EB3FCC54-03B1-44CC-9E40-FD0CBAEE391C"), 1
    ),
    "area500_wf5_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("F9176D07-F485-41D8-900A-07CE7B410D13"), 1
    ),
    "area500_wf6_blaine_b": AreaAnalyzeClass(
        uuid.UUID("EACCFA12-1197-4D30-827D-10EA8821C8FC"), 1
    ),
    "area500_wf6_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("9BCF9AB5-3E2C-4F9A-B934-004BEB55E9E6"), 1
    ),
    "area500_wf6_blaine_e": AreaAnalyzeClass(
        uuid.UUID("D2CE54B4-569C-4705-A661-FC43EADF8D43"), 1
    ),
    "area500_wf6_blaine_es": AreaAnalyzeClass(
        uuid.UUID("F208A2D7-AA1F-46AC-9550-F7B85F5D8067"), 1
    ),
    "area500_wf6_blaine_p": AreaAnalyzeClass(
        uuid.UUID("7807A2B7-77F5-44C7-8E60-16D57D204CAF"), 1
    ),
    "area500_wf6_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("B63B4E5C-7F54-42FE-8DA1-FA09630168C9"), 1
    ),
    "area500_wf6_blaine_result": AreaAnalyzeClass(
        uuid.UUID("623A0B63-B09F-4C10-B986-8AD91FDA1ED2"), 2
    ),
    "area500_wf6_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("F1FA5ED8-DB8C-4D0A-B03B-16AB3937095A"), 1
    ),
    "area500_wf6_blaine_t": AreaAnalyzeClass(
        uuid.UUID("00161B92-F182-4BEF-AB34-5CF829E76453"), 1
    ),
    "area500_wf6_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("18943E7E-A79C-4B32-A216-02272ABBA0B2"), 1
    ),
    "area500_wf6_feo_avg": AreaAnalyzeClass(
        uuid.UUID("BA6AA62B-FAA5-4CD4-BB33-3DB82A2B10B4"), 2
    ),
    "area500_wf6_feo_input1": AreaAnalyzeClass(
        uuid.UUID("BC6C5EAE-3634-440B-A78C-070D5A2E5F50"), 1
    ),
    "area500_wf6_feo_input2": AreaAnalyzeClass(
        uuid.UUID("80A3663E-C2B1-4A73-8A21-5E95E92DA4D4"), 1
    ),
    "area500_wf6_moisture_input": AreaAnalyzeClass(
        uuid.UUID("61788DFE-2D22-4D78-98F8-198F7F6E60CB"), 1
    ),
    "area500_wf6_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("A34EF638-D8F4-43F4-A4C9-60F40F338108"), 2
    ),
    "area500_wf6_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("FB48D801-A4D8-47D6-9A0D-1BD4D6CCDE04"), 1
    ),
    "area500_wf6_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("61212A42-F4D0-4E25-9252-FC50E819787E"), 1
    ),
    "area500_wf7_moisture_input": AreaAnalyzeClass(
        uuid.UUID("53A1D56B-0D67-4DA7-9A69-56C37A7E60E3"), 1
    ),
    "area500_wf8_moisture_input": AreaAnalyzeClass(
        uuid.UUID("4F22ED5B-AD51-416C-98CE-8274C1E9D088"), 1
    ),
    "area500_wf9_moisture_input": AreaAnalyzeClass(
        uuid.UUID("74B598BA-ADF6-4888-A2F4-4CF3A0397674"), 1
    ),
    "area600_gratefeed_drop_avg": AreaAnalyzeClass(
        uuid.UUID("D7126E57-885B-434D-B6EF-925B573825A5"), 2
    ),
    "area600_gratefeed_drop_input1 ": AreaAnalyzeClass(
        uuid.UUID("4467BC1B-F4F1-45A0-B4B4-60D76D3DF7F1"), 1
    ),
    "area600_gratefeed_drop_input10": AreaAnalyzeClass(
        uuid.UUID("7E2F22D9-E020-4681-826E-A1791B732FBA"), 1
    ),
    "area600_gratefeed_drop_input11": AreaAnalyzeClass(
        uuid.UUID("BB199033-96A6-4C8B-BA88-A57CE10FB889"), 1
    ),
    "area600_gratefeed_drop_input12": AreaAnalyzeClass(
        uuid.UUID("FBCD999F-E55A-4177-B793-4E4C6FFCD5B5"), 1
    ),
    "area600_gratefeed_drop_input2 ": AreaAnalyzeClass(
        uuid.UUID("29ADD09F-4547-4FB2-A7A6-8AF33CF39946"), 1
    ),
    "area600_gratefeed_drop_input3 ": AreaAnalyzeClass(
        uuid.UUID("94D02813-EDB0-4972-BC92-FD92A326CE2E"), 1
    ),
    "area600_gratefeed_drop_input4 ": AreaAnalyzeClass(
        uuid.UUID("6C55118F-D8BB-4376-8AF3-852626C59DED"), 1
    ),
    "area600_gratefeed_drop_input5": AreaAnalyzeClass(
        uuid.UUID("9EBB6F0D-EDB3-4917-9C04-00089C5AD6C3"), 1
    ),
    "area600_gratefeed_drop_input6 ": AreaAnalyzeClass(
        uuid.UUID("772F03C6-FC0D-464C-B2F9-EF7F7E8CC7BB"), 1
    ),
    "area600_gratefeed_drop_input7 ": AreaAnalyzeClass(
        uuid.UUID("6440BE16-6FE8-4795-8B7F-8E67C688C2C1"), 1
    ),
    "area600_gratefeed_drop_input8 ": AreaAnalyzeClass(
        uuid.UUID("A5CBA20C-39C8-4DD7-A700-0A0F81031666"), 1
    ),
    "area600_gratefeed_drop_input9 ": AreaAnalyzeClass(
        uuid.UUID("4CB0B3FC-9386-44EF-915A-1B7E527C0300"), 1
    ),
    "area600_gratefeed_drop_std": AreaAnalyzeClass(
        uuid.UUID("31414FAB-C3E8-4FD4-BCC0-4EE6405F3FB7"), 2
    ),
    "area600_gratefeed_gcs_avg": AreaAnalyzeClass(
        uuid.UUID("D038DBED-9D51-48EC-95EC-2DE930EB7D51"), 2
    ),
    "area600_gratefeed_gcs_input1 ": AreaAnalyzeClass(
        uuid.UUID("17ADEB82-995D-4C99-9847-E46D29992345"), 1
    ),
    "area600_gratefeed_gcs_input10": AreaAnalyzeClass(
        uuid.UUID("E4BE1F4E-E928-4F41-999E-7B3D5EED82E1"), 1
    ),
    "area600_gratefeed_gcs_input11": AreaAnalyzeClass(
        uuid.UUID("06234749-C835-48A0-A1B7-F6AA478527B8"), 1
    ),
    "area600_gratefeed_gcs_input12": AreaAnalyzeClass(
        uuid.UUID("A2D89106-7A45-40EC-BFBF-8410E22B3656"), 1
    ),
    "area600_gratefeed_gcs_input2 ": AreaAnalyzeClass(
        uuid.UUID("2B869DC4-36C5-4BB1-AE88-6FF305DFD19A"), 1
    ),
    "area600_gratefeed_gcs_input3 ": AreaAnalyzeClass(
        uuid.UUID("A8CA2BD1-B833-49AA-96D0-3B1F239056D4"), 1
    ),
    "area600_gratefeed_gcs_input4 ": AreaAnalyzeClass(
        uuid.UUID("ABB5B8EB-B5B7-4625-9ABE-7D80FDBBBC87"), 1
    ),
    "area600_gratefeed_gcs_input5 ": AreaAnalyzeClass(
        uuid.UUID("1131CF72-85CA-4233-A851-5963A4A96973"), 1
    ),
    "area600_gratefeed_gcs_input6 ": AreaAnalyzeClass(
        uuid.UUID("F564269C-BA5A-43F0-9ABC-B30C645787E5"), 1
    ),
    "area600_gratefeed_gcs_input7 ": AreaAnalyzeClass(
        uuid.UUID("C5E09EF2-96CF-4DEB-9834-D9AA00504C1E"), 1
    ),
    "area600_gratefeed_gcs_input8 ": AreaAnalyzeClass(
        uuid.UUID("EA967216-D2E7-4DFB-A9B0-FA402D370B71"), 1
    ),
    "area600_gratefeed_gcs_input9 ": AreaAnalyzeClass(
        uuid.UUID("1195D123-15DE-433B-8106-59B13350D9C7"), 1
    ),
    "area600_gratefeed_gcs_std": AreaAnalyzeClass(
        uuid.UUID("834060B7-4060-41C8-9663-B15DCCA38249"), 2
    ),
    "area600_gratefeed_moisture_input": AreaAnalyzeClass(
        uuid.UUID("B0FDEC45-80DC-4FF9-B754-603881377C10"), 1
    ),
    "area600_gratefeed_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("EDB85E8C-F9C9-4F99-9919-378D42C812A1"), 1
    ),
    "area600_gratefeed_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("224F72ED-59BB-40A4-8499-777430BF98A9"), 2
    ),
    "area600_gratefeed_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("659C61CD-ABF0-498F-BFE2-647EE9750DEB"), 1
    ),
    "area600_gratefeed_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("6447CC7C-ACDF-43D1-B9EA-4D4EA99968FD"), 2
    ),
    "area600_gratefeed_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("7569BA7B-64CB-4C03-8ED2-CD554503C4D0"), 1
    ),
    "area600_gratefeed_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("850AFE44-0BB9-4AB9-ADCF-78D510EE3D22"), 2
    ),
    "area600_gratefeed_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("14C8031D-5A59-4AEF-BB29-96108C5563FE"), 1
    ),
    "area600_gratefeed_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("AF7473FB-820B-4CF0-B0D9-EC1DD9ACF624"), 2
    ),
    "area600_gratefeed_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("8011B320-030D-421D-ADA0-52577A2E92D5"), 1
    ),
    "area600_gratefeed_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("C26749DE-691C-42B1-9A3F-96891D6D61FE"), 2
    ),
    "area600_gratefeed_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("7EBD71AD-9BBA-4E6A-8E1F-10DA8F6F1863"), 1
    ),
    "area600_rfundersize_drop_avg": AreaAnalyzeClass(
        uuid.UUID("F2E67CF7-B3B6-4F77-8407-C52911F2DDBA"), 2
    ),
    "area600_rfundersize_drop_input1 ": AreaAnalyzeClass(
        uuid.UUID("46ED93D8-C52D-443B-926E-1670FE729239"), 1
    ),
    "area600_rfundersize_drop_input10": AreaAnalyzeClass(
        uuid.UUID("906A9D42-9917-4831-924E-306EBB3FB31A"), 1
    ),
    "area600_rfundersize_drop_input11": AreaAnalyzeClass(
        uuid.UUID("53D45CA0-6D45-4A2A-938C-7757649D1BD1"), 1
    ),
    "area600_rfundersize_drop_input12": AreaAnalyzeClass(
        uuid.UUID("0640670D-4FE0-4C3D-B199-DC0C5B7262BB"), 1
    ),
    "area600_rfundersize_drop_input2 ": AreaAnalyzeClass(
        uuid.UUID("28E2D2C6-2640-4B22-9916-1F027E949285"), 1
    ),
    "area600_rfundersize_drop_input3 ": AreaAnalyzeClass(
        uuid.UUID("F0224A8A-CA09-49E8-BFD5-7E8871FB9BEA"), 1
    ),
    "area600_rfundersize_drop_input4 ": AreaAnalyzeClass(
        uuid.UUID("2D29812E-3274-47C0-A91A-9FFABEA95C9B"), 1
    ),
    "area600_rfundersize_drop_input5": AreaAnalyzeClass(
        uuid.UUID("2D775413-70A0-46A6-963E-C05BE9756D2A"), 1
    ),
    "area600_rfundersize_drop_input6 ": AreaAnalyzeClass(
        uuid.UUID("8428BDB8-C214-449E-A2A6-2EA080C2E9B5"), 1
    ),
    "area600_rfundersize_drop_input7 ": AreaAnalyzeClass(
        uuid.UUID("236108C9-CE34-4377-A25B-9245F8D4EF2D"), 1
    ),
    "area600_rfundersize_drop_input8 ": AreaAnalyzeClass(
        uuid.UUID("FDE0E380-897C-4F7D-BBFF-B195F6B0EA09"), 1
    ),
    "area600_rfundersize_drop_input9 ": AreaAnalyzeClass(
        uuid.UUID("1E0B704B-252C-47F8-AEA3-81FC31135F0F"), 1
    ),
    "area600_rfundersize_drop_std": AreaAnalyzeClass(
        uuid.UUID("C7D33714-8700-43B0-A5E0-E7C6836CAC61"), 2
    ),
    "area600_rfundersize_gcs_avg": AreaAnalyzeClass(
        uuid.UUID("4F94E05C-8C62-4AA5-8D65-9603004AD895"), 2
    ),
    "area600_rfundersize_gcs_input1 ": AreaAnalyzeClass(
        uuid.UUID("CE4B7650-68A7-41BE-815C-B15954EA9EB4"), 1
    ),
    "area600_rfundersize_gcs_input10": AreaAnalyzeClass(
        uuid.UUID("B9B959EB-A8BF-457E-9327-776A0B93F922"), 1
    ),
    "area600_rfundersize_gcs_input11": AreaAnalyzeClass(
        uuid.UUID("1AF6EB83-79E1-4E92-9C50-22672213B2A0"), 1
    ),
    "area600_rfundersize_gcs_input12": AreaAnalyzeClass(
        uuid.UUID("45EE1621-6F89-440E-8D0A-4C9E003692FC"), 1
    ),
    "area600_rfundersize_gcs_input2 ": AreaAnalyzeClass(
        uuid.UUID("BF0E2430-8B1C-47D5-96C1-79944EC293A2"), 1
    ),
    "area600_rfundersize_gcs_input3 ": AreaAnalyzeClass(
        uuid.UUID("FD6DC57C-8468-4C37-90E9-265010095808"), 1
    ),
    "area600_rfundersize_gcs_input4 ": AreaAnalyzeClass(
        uuid.UUID("EAF2B763-DF91-490A-99FA-01B73FEBE3D9"), 1
    ),
    "area600_rfundersize_gcs_input5 ": AreaAnalyzeClass(
        uuid.UUID("C4056299-003F-46B1-AC34-DD093D439C2D"), 1
    ),
    "area600_rfundersize_gcs_input6 ": AreaAnalyzeClass(
        uuid.UUID("A432BBE8-2E74-4DFC-BDBE-0753B46ECBD0"), 1
    ),
    "area600_rfundersize_gcs_input7 ": AreaAnalyzeClass(
        uuid.UUID("C0B56D64-01E7-4FB9-9E35-51C1F02EC185"), 1
    ),
    "area600_rfundersize_gcs_input8 ": AreaAnalyzeClass(
        uuid.UUID("0756A81C-81FB-4016-BAF0-46D19C1C9627"), 1
    ),
    "area600_rfundersize_gcs_input9 ": AreaAnalyzeClass(
        uuid.UUID("85D48942-6D2A-4E3B-A1C6-B3603D57DC95"), 1
    ),
    "area600_rfundersize_gcs_std": AreaAnalyzeClass(
        uuid.UUID("61E374BC-610B-4F08-A49F-685DE724EB9F"), 2
    ),
    "area600_rfundersize_moisture_input": AreaAnalyzeClass(
        uuid.UUID("1E0435BE-229A-4E03-8DC8-07C9FF9C8137"), 1
    ),
    "area600_rfundersize_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("FABDF5BA-8702-401D-955E-44C01D943D8D"), 1
    ),
    "area600_rfundersize_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("B2FF1BFC-C980-476E-9085-707DB9027D09"), 2
    ),
    "area600_rfundersize_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("CA3D5064-FA37-4C2A-9BD6-775B21902F2F"), 1
    ),
    "area600_rfundersize_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("FCC48BC3-8F56-406C-8127-E7B33BAEC2D6"), 2
    ),
    "area600_rfundersize_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("5BE2EFB1-24AB-450C-9F24-54A672B110C3"), 1
    ),
    "area600_rfundersize_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("461E8C75-B5DF-4E78-B235-EFB2E3FA7478"), 2
    ),
    "area600_rfundersize_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("B724B11D-8770-4022-824D-6A09823E1D4B"), 1
    ),
    "area600_rfundersize_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("047AB7A1-38A4-423D-9510-453497ED436A"), 2
    ),
    "area600_rfundersize_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("C6E91965-735B-46D7-90C0-80C330C32171"), 1
    ),
    "area600_rfundersize_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("C94FA864-2FD7-4D2B-8933-C17F78ABA657"), 2
    ),
    "area600_rfundersize_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("D2F70837-62FC-4F7D-A103-92C361E1681E"), 1
    ),
    "area800_810_atomic_k2o": AreaAnalyzeClass(
        uuid.UUID("DC12E75E-1D95-4A51-B061-5118E1D42E0B"), 1
    ),
    "area800_810_atomic_na2o": AreaAnalyzeClass(
        uuid.UUID("FD1FCF21-C252-431F-9DC8-8615FA53242F"), 1
    ),
    "area800_810_ccs_100": AreaAnalyzeClass(
        uuid.UUID("30E33E9F-0DD3-4E94-A154-2A8053F28EBF"), 2
    ),
    "area800_810_ccs_150": AreaAnalyzeClass(
        uuid.UUID("CB4887AE-C0CE-4655-B435-9AF99B930423"), 2
    ),
    "area800_810_ccs_50": AreaAnalyzeClass(
        uuid.UUID("9352F98C-ECBA-458A-BC2E-BB0A63AAF064"), 2
    ),
    "area800_810_ccs_avg": AreaAnalyzeClass(
        uuid.UUID("77127419-D5B5-47BD-B0C8-DC13C2A24C66"), 2
    ),
    "area800_810_ccs_description": AreaAnalyzeClass(
        uuid.UUID("D7AD221D-544A-4244-B9AC-7624990E7E90"), 1
    ),
    "area800_810_ccs_input1": AreaAnalyzeClass(
        uuid.UUID("0EB2DB94-57DE-40D1-9076-734EE42D7604"), 1
    ),
    "area800_810_ccs_input10": AreaAnalyzeClass(
        uuid.UUID("0CB341B9-3646-4FFA-A0AE-7F72ED8C0504"), 1
    ),
    "area800_810_ccs_input100": AreaAnalyzeClass(
        uuid.UUID("6223BDF1-48F5-4E11-868F-60103159621A"), 1
    ),
    "area800_810_ccs_input11": AreaAnalyzeClass(
        uuid.UUID("8C40BF5B-BE58-434E-B29B-4A598810B5BF"), 1
    ),
    "area800_810_ccs_input12": AreaAnalyzeClass(
        uuid.UUID("C5784249-C21A-461D-9479-80FBF3685674"), 1
    ),
    "area800_810_ccs_input13": AreaAnalyzeClass(
        uuid.UUID("5FF7106A-9AC7-4B37-92D9-7E54972AF5DF"), 1
    ),
    "area800_810_ccs_input14": AreaAnalyzeClass(
        uuid.UUID("F7223CC6-F4F2-432C-8155-5A5601123566"), 1
    ),
    "area800_810_ccs_input15": AreaAnalyzeClass(
        uuid.UUID("F557BA22-E3E3-4A59-8381-E3D0E10BFAB3"), 1
    ),
    "area800_810_ccs_input16": AreaAnalyzeClass(
        uuid.UUID("55830BC7-D628-49C7-B484-E895CD4206D3"), 1
    ),
    "area800_810_ccs_input17": AreaAnalyzeClass(
        uuid.UUID("778AD458-FF65-45D5-B14D-98FCC1E24202"), 1
    ),
    "area800_810_ccs_input18": AreaAnalyzeClass(
        uuid.UUID("9BE0B528-7707-491D-A81C-B591CD151509"), 1
    ),
    "area800_810_ccs_input19": AreaAnalyzeClass(
        uuid.UUID("2B519C86-7CE9-4E9F-996A-12F14B24C636"), 1
    ),
    "area800_810_ccs_input2": AreaAnalyzeClass(
        uuid.UUID("53FF0F00-676E-40A7-90E8-A17B5582ED00"), 1
    ),
    "area800_810_ccs_input20": AreaAnalyzeClass(
        uuid.UUID("A58A15A5-48E3-4551-8427-F9B7E4D22266"), 1
    ),
    "area800_810_ccs_input21": AreaAnalyzeClass(
        uuid.UUID("870B68D6-5EB3-422F-A147-355E594BE916"), 1
    ),
    "area800_810_ccs_input22": AreaAnalyzeClass(
        uuid.UUID("BF9748F6-8EEA-4B17-9D7B-5947FCB6781B"), 1
    ),
    "area800_810_ccs_input23": AreaAnalyzeClass(
        uuid.UUID("E4DF41F6-162F-428D-8E0C-EC420C766694"), 1
    ),
    "area800_810_ccs_input24": AreaAnalyzeClass(
        uuid.UUID("810673A6-54BA-4B6E-BA78-1E458E2DAC65"), 1
    ),
    "area800_810_ccs_input25": AreaAnalyzeClass(
        uuid.UUID("C3C80F6E-0038-458D-8F5C-0A60F945E591"), 1
    ),
    "area800_810_ccs_input26": AreaAnalyzeClass(
        uuid.UUID("099E62B2-5A85-45B7-96A9-4FF571374879"), 1
    ),
    "area800_810_ccs_input27": AreaAnalyzeClass(
        uuid.UUID("12CC4E53-FF3B-4425-838F-F29A5B5E17CF"), 1
    ),
    "area800_810_ccs_input28": AreaAnalyzeClass(
        uuid.UUID("6658CFF4-3C86-4D94-A7C7-3F0EEDBF972C"), 1
    ),
    "area800_810_ccs_input29": AreaAnalyzeClass(
        uuid.UUID("73FE2BEE-1159-49D8-A9D2-8AA9695D965B"), 1
    ),
    "area800_810_ccs_input3": AreaAnalyzeClass(
        uuid.UUID("FB87C66A-83F2-405F-A27A-5C79BB539FE1"), 1
    ),
    "area800_810_ccs_input30": AreaAnalyzeClass(
        uuid.UUID("C27625AD-F91D-4166-91FE-A9C2C80BC28B"), 1
    ),
    "area800_810_ccs_input31": AreaAnalyzeClass(
        uuid.UUID("173DBBF3-6A1E-40B6-9C00-2FCC4B83B6CD"), 1
    ),
    "area800_810_ccs_input32": AreaAnalyzeClass(
        uuid.UUID("5BA39BFF-FBE1-47A1-A3C2-5BCF516B424E"), 1
    ),
    "area800_810_ccs_input33": AreaAnalyzeClass(
        uuid.UUID("0AA393CE-250A-46DF-A69C-17B2EAEE3AED"), 1
    ),
    "area800_810_ccs_input34": AreaAnalyzeClass(
        uuid.UUID("7A7B88D5-F1AF-43A0-9F27-224339C93727"), 1
    ),
    "area800_810_ccs_input35": AreaAnalyzeClass(
        uuid.UUID("C01F14E1-57E1-4990-95FD-191F806C3082"), 1
    ),
    "area800_810_ccs_input36": AreaAnalyzeClass(
        uuid.UUID("2E8A5898-CAD5-468C-AEDA-4A5B8B1494B7"), 1
    ),
    "area800_810_ccs_input37": AreaAnalyzeClass(
        uuid.UUID("BEB37BB6-821E-4C88-8E1B-8FB963E7AE75"), 1
    ),
    "area800_810_ccs_input38": AreaAnalyzeClass(
        uuid.UUID("9B473919-DBA3-4152-9A8A-48EAF4A3262B"), 1
    ),
    "area800_810_ccs_input39": AreaAnalyzeClass(
        uuid.UUID("9CF51C30-8A84-4772-86AB-4AB0DA951210"), 1
    ),
    "area800_810_ccs_input4": AreaAnalyzeClass(
        uuid.UUID("3DEE0F42-A37B-4502-87FC-2518AA246F02"), 1
    ),
    "area800_810_ccs_input40": AreaAnalyzeClass(
        uuid.UUID("C36CF338-72A1-42CF-BD44-C87BEE740F64"), 1
    ),
    "area800_810_ccs_input41": AreaAnalyzeClass(
        uuid.UUID("EA635C95-9591-4AA7-AFCE-4B7A12A9D316"), 1
    ),
    "area800_810_ccs_input42": AreaAnalyzeClass(
        uuid.UUID("BDC99736-89C9-428F-9EDC-44939DD12975"), 1
    ),
    "area800_810_ccs_input43": AreaAnalyzeClass(
        uuid.UUID("6E3A8A16-92DC-45E1-B2E2-A9CF43F6C35B"), 1
    ),
    "area800_810_ccs_input44": AreaAnalyzeClass(
        uuid.UUID("F36D69C1-8438-40BA-8C32-DF9DB565B7FD"), 1
    ),
    "area800_810_ccs_input45": AreaAnalyzeClass(
        uuid.UUID("E8330C8B-ADCC-4EFE-B60B-A3B3A923132D"), 1
    ),
    "area800_810_ccs_input46": AreaAnalyzeClass(
        uuid.UUID("AB657C6C-264C-4809-B1D3-7CDB03AE1F0F"), 1
    ),
    "area800_810_ccs_input47": AreaAnalyzeClass(
        uuid.UUID("DAE1E246-7306-4277-8AF6-24467A26896C"), 1
    ),
    "area800_810_ccs_input48": AreaAnalyzeClass(
        uuid.UUID("56E54045-AE2D-4E33-9BA6-D4C5536E2BDA"), 1
    ),
    "area800_810_ccs_input49": AreaAnalyzeClass(
        uuid.UUID("5F161078-CB84-4C47-8EFD-D25B32888C28"), 1
    ),
    "area800_810_ccs_input5": AreaAnalyzeClass(
        uuid.UUID("C4B1A624-0006-4169-8B08-E772926F5F19"), 1
    ),
    "area800_810_ccs_input50": AreaAnalyzeClass(
        uuid.UUID("79280349-A2F2-46E4-97A9-E45D3496FF52"), 1
    ),
    "area800_810_ccs_input51": AreaAnalyzeClass(
        uuid.UUID("2946266F-6CAF-4AAA-B223-E03E4B590AD9"), 1
    ),
    "area800_810_ccs_input52": AreaAnalyzeClass(
        uuid.UUID("0517CAD6-29E2-445B-9D49-378FF6F8D820"), 1
    ),
    "area800_810_ccs_input53": AreaAnalyzeClass(
        uuid.UUID("2C18E87B-B041-4FDE-99C7-B08D692B9485"), 1
    ),
    "area800_810_ccs_input54": AreaAnalyzeClass(
        uuid.UUID("7AD77EB3-FA63-42F5-981C-444C4DFE26DC"), 1
    ),
    "area800_810_ccs_input55": AreaAnalyzeClass(
        uuid.UUID("9A933877-ACB7-462F-8894-1551940965D6"), 1
    ),
    "area800_810_ccs_input56": AreaAnalyzeClass(
        uuid.UUID("24BCB2F7-3D3B-4D59-80CD-F67B8078B0B4"), 1
    ),
    "area800_810_ccs_input57": AreaAnalyzeClass(
        uuid.UUID("0AD57929-8D7D-41CF-9D3E-0C8361341C23"), 1
    ),
    "area800_810_ccs_input58": AreaAnalyzeClass(
        uuid.UUID("716877B7-DF04-4038-A41B-8A917C6764CC"), 1
    ),
    "area800_810_ccs_input59": AreaAnalyzeClass(
        uuid.UUID("8C4DFE72-A538-41CB-859F-FCFD63EFC60D"), 1
    ),
    "area800_810_ccs_input6": AreaAnalyzeClass(
        uuid.UUID("78F6444E-C943-4E35-8807-79DD2307CC9B"), 1
    ),
    "area800_810_ccs_input60": AreaAnalyzeClass(
        uuid.UUID("E54A2E0F-2598-4F50-A2B7-AE393B6EF203"), 1
    ),
    "area800_810_ccs_input61": AreaAnalyzeClass(
        uuid.UUID("3C864034-2760-4F8C-BF37-6FE2A1FF83DF"), 1
    ),
    "area800_810_ccs_input62": AreaAnalyzeClass(
        uuid.UUID("FF6853F6-3F14-4FA3-87DE-D8F1744543B3"), 1
    ),
    "area800_810_ccs_input63": AreaAnalyzeClass(
        uuid.UUID("7DE4D919-9942-4DFA-A37D-8C05046C7969"), 1
    ),
    "area800_810_ccs_input64": AreaAnalyzeClass(
        uuid.UUID("471E0D5A-4825-4AD9-BCDD-362A264F67E2"), 1
    ),
    "area800_810_ccs_input65": AreaAnalyzeClass(
        uuid.UUID("249A42FF-B344-4D83-844F-DA8BE2AC5AFF"), 1
    ),
    "area800_810_ccs_input66": AreaAnalyzeClass(
        uuid.UUID("0D8C8E35-EDD9-4B36-B227-C83C2B7EB0B2"), 1
    ),
    "area800_810_ccs_input67": AreaAnalyzeClass(
        uuid.UUID("B803F668-B096-40DA-8E3C-509F60842706"), 1
    ),
    "area800_810_ccs_input68": AreaAnalyzeClass(
        uuid.UUID("744A057C-C04A-466F-B64A-6278A190B947"), 1
    ),
    "area800_810_ccs_input69": AreaAnalyzeClass(
        uuid.UUID("EAEB4C32-F500-41E4-9B00-177BEBF93426"), 1
    ),
    "area800_810_ccs_input7": AreaAnalyzeClass(
        uuid.UUID("E5AC15FA-5570-4D17-A857-D371E7C2823A"), 1
    ),
    "area800_810_ccs_input70": AreaAnalyzeClass(
        uuid.UUID("AC3C576A-A751-4D2C-A045-5243A56850C1"), 1
    ),
    "area800_810_ccs_input71": AreaAnalyzeClass(
        uuid.UUID("47775860-2B57-4575-BCD1-0FC1ABFCA875"), 1
    ),
    "area800_810_ccs_input72": AreaAnalyzeClass(
        uuid.UUID("98D4D20C-3166-4293-BE73-76D7B662E6C6"), 1
    ),
    "area800_810_ccs_input73": AreaAnalyzeClass(
        uuid.UUID("A89CE8D1-0A02-4C8E-8658-53DA801C3326"), 1
    ),
    "area800_810_ccs_input74": AreaAnalyzeClass(
        uuid.UUID("B603BA0C-C208-4A4B-ACE0-5C377C3F7061"), 1
    ),
    "area800_810_ccs_input75": AreaAnalyzeClass(
        uuid.UUID("DEC92B58-1EFE-4055-AB0D-B5F804947823"), 1
    ),
    "area800_810_ccs_input76": AreaAnalyzeClass(
        uuid.UUID("32CE1C66-67BA-4F47-8AED-C482E61C361B"), 1
    ),
    "area800_810_ccs_input77": AreaAnalyzeClass(
        uuid.UUID("E8D7A7F2-213B-48CA-999B-E1F86CD90664"), 1
    ),
    "area800_810_ccs_input78": AreaAnalyzeClass(
        uuid.UUID("AA85F232-A9B9-4E01-8213-C7ACCC8C8134"), 1
    ),
    "area800_810_ccs_input79": AreaAnalyzeClass(
        uuid.UUID("B921728D-92E4-4C1C-9B1C-0FE3EF109844"), 1
    ),
    "area800_810_ccs_input8": AreaAnalyzeClass(
        uuid.UUID("604B0C39-5BB3-4EFB-B710-882D59411B7C"), 1
    ),
    "area800_810_ccs_input80": AreaAnalyzeClass(
        uuid.UUID("3F57443B-97BA-4442-9847-99A8CC61D9A2"), 1
    ),
    "area800_810_ccs_input81": AreaAnalyzeClass(
        uuid.UUID("54F61D0F-1AE2-435A-9E0F-67717977776B"), 1
    ),
    "area800_810_ccs_input82": AreaAnalyzeClass(
        uuid.UUID("C6C74DCE-931A-4864-92C7-9348295ECD6E"), 1
    ),
    "area800_810_ccs_input83": AreaAnalyzeClass(
        uuid.UUID("F6B96687-D75A-4B10-8B5E-A3A5E57AAE3B"), 1
    ),
    "area800_810_ccs_input84": AreaAnalyzeClass(
        uuid.UUID("EC2E906C-DA45-44CC-A964-D7BC5822CA35"), 1
    ),
    "area800_810_ccs_input85": AreaAnalyzeClass(
        uuid.UUID("AC26C378-F0AF-4460-9F32-B0800C288D0D"), 1
    ),
    "area800_810_ccs_input86": AreaAnalyzeClass(
        uuid.UUID("570F2F6A-808C-41CB-9BBB-FCD7EB8A614E"), 1
    ),
    "area800_810_ccs_input87": AreaAnalyzeClass(
        uuid.UUID("CD6BF9F3-FB88-467A-94E6-6C2816E37170"), 1
    ),
    "area800_810_ccs_input88": AreaAnalyzeClass(
        uuid.UUID("E9E52CFC-7FE7-4ED0-B449-984D6F157946"), 1
    ),
    "area800_810_ccs_input89": AreaAnalyzeClass(
        uuid.UUID("43DCDCAC-54B6-49A0-B899-9DEBCFA9A16C"), 1
    ),
    "area800_810_ccs_input9": AreaAnalyzeClass(
        uuid.UUID("D6DF45E1-44E5-4DAB-A6CA-C9D0737397C2"), 1
    ),
    "area800_810_ccs_input90": AreaAnalyzeClass(
        uuid.UUID("7F65C90B-BAEE-48B8-B741-5FA96C5C02E5"), 1
    ),
    "area800_810_ccs_input91": AreaAnalyzeClass(
        uuid.UUID("0A534739-82E8-471C-A166-F6FB5A9B496E"), 1
    ),
    "area800_810_ccs_input92": AreaAnalyzeClass(
        uuid.UUID("6397DE16-DB49-4B62-98D2-7ACA155BE2B3"), 1
    ),
    "area800_810_ccs_input93": AreaAnalyzeClass(
        uuid.UUID("B7AFA751-F2B3-42D3-AC04-66D7BC576F00"), 1
    ),
    "area800_810_ccs_input94": AreaAnalyzeClass(
        uuid.UUID("87DA5ACF-946F-4E6B-BF3C-3C6929FCC663"), 1
    ),
    "area800_810_ccs_input95": AreaAnalyzeClass(
        uuid.UUID("33578433-5F89-438D-BD11-6754B4126F4B"), 1
    ),
    "area800_810_ccs_input96": AreaAnalyzeClass(
        uuid.UUID("F143F6B7-EFFD-496A-924B-2EC8B35685A1"), 1
    ),
    "area800_810_ccs_input97": AreaAnalyzeClass(
        uuid.UUID("B5494BAA-8A93-4A0A-9FA7-32655689F9EF"), 1
    ),
    "area800_810_ccs_input98": AreaAnalyzeClass(
        uuid.UUID("C50F59BB-4F75-4B0A-AEED-F62E02A224F4"), 1
    ),
    "area800_810_ccs_input99": AreaAnalyzeClass(
        uuid.UUID("E0DEC605-EAC7-46FD-A0DD-71035BDF4828"), 1
    ),
    "area800_810_ccs_std": AreaAnalyzeClass(
        uuid.UUID("093649C3-208A-4AE3-BF03-EAE619BF4325"), 2
    ),
    "area800_810_description_input1": AreaAnalyzeClass(
        uuid.UUID("C0C3332A-A212-499F-8541-4F3764B58074"), 1
    ),
    "area800_810_feo_avg": AreaAnalyzeClass(
        uuid.UUID("FC44BE13-9E11-4834-B060-2C9063E96842"), 2
    ),
    "area800_810_feo_input1": AreaAnalyzeClass(
        uuid.UUID("0CB72A5B-8455-45FB-8EF2-9818920C5A22"), 1
    ),
    "area800_810_feo_input2": AreaAnalyzeClass(
        uuid.UUID("6716AFFA-9A06-47DC-9BEE-499265BD4BCB"), 1
    ),
    "area800_810_moisture_input": AreaAnalyzeClass(
        uuid.UUID("5E0150F4-CF85-4E36-BBAC-43733C2F2536"), 1
    ),
    "area800_810_porosity_dry": AreaAnalyzeClass(
        uuid.UUID("72E4899A-56B4-4932-9807-E202CF87DD9A"), 1
    ),
    "area800_810_porosity_result": AreaAnalyzeClass(
        uuid.UUID("8694CF34-E729-4CA8-92C8-0B42855B1824"), 2
    ),
    "area800_810_porosity_saturated": AreaAnalyzeClass(
        uuid.UUID("AE24A83C-4C31-42E3-9A47-305F0BE61EC9"), 1
    ),
    "area800_810_porosity_suspended": AreaAnalyzeClass(
        uuid.UUID("B893DBDC-C715-43A8-A262-015473EC51BD"), 1
    ),
    "area800_810_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("5128B5FB-B876-4A99-9151-387B5BED92C6"), 1
    ),
    "area800_810_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("24152E48-3ADA-4DB5-BA79-6DAF3867CC75"), 2
    ),
    "area800_810_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("5961F48D-EC27-4132-8B0A-D40D9BC2F868"), 1
    ),
    "area800_810_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("6F83D90A-6613-439F-ABAF-E2CF01B60A97"), 2
    ),
    "area800_810_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("998C51BB-7CE6-455C-8314-A1118D609EA4"), 1
    ),
    "area800_810_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("7EA48BA3-BE72-4291-9082-E6A355443FA7"), 2
    ),
    "area800_810_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("7B2E1DDB-FFCF-4F19-9261-5BC1AE081038"), 1
    ),
    "area800_810_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("B49A96D5-D131-43E0-9E7D-BE14C4864901"), 2
    ),
    "area800_810_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("85AE4E02-75BB-40D6-823E-7F248B5BEACC"), 1
    ),
    "area800_810_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("4B4436BB-003A-4836-9389-5F12282DEF5E"), 2
    ),
    "area800_810_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("2BBAC1F9-4BF7-43DD-8DAF-312BEC6BA8BB"), 1
    ),
    "area800_810_sulfur_input": AreaAnalyzeClass(
        uuid.UUID("5B3954E5-BFC6-4498-8C99-FB4883277037"), 1
    ),
    "area800_810_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("B355482B-517C-4E5A-9943-BA66DC1B35D2"), 2
    ),
    "area800_810_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("137B0CEA-8C7E-4FCC-B986-130FC47C116B"), 1
    ),
    "area800_810_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("AD6F3D05-0F84-45DA-BEB8-17CE0F23482D"), 1
    ),
    "area800_810_tumble_r5w": AreaAnalyzeClass(
        uuid.UUID("41602DFA-890F-4993-974A-B38CA3020E7C"), 2
    ),
    "area800_810_tumble_r63w": AreaAnalyzeClass(
        uuid.UUID("21AFC759-775A-4F51-AAAF-8552E73C442C"), 2
    ),
    "area800_810_tumble_remain5": AreaAnalyzeClass(
        uuid.UUID("A4D829AD-FF84-4C0B-B446-5488E4FEFB28"), 1
    ),
    "area800_810_tumble_remain63": AreaAnalyzeClass(
        uuid.UUID("DA1BEF43-C917-4018-86F2-C3B0807AC072"), 1
    ),
    "area800_810_tumble_weight": AreaAnalyzeClass(
        uuid.UUID("7F41C2FE-268A-4BA3-A7A3-264CCD5A3835"), 1
    ),
    "area800_810_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("951050B5-A053-4D4E-9846-652109038189"), 1
    ),
    "area800_810_xray_cao": AreaAnalyzeClass(
        uuid.UUID("ACA4D255-6D21-4C80-9EFD-7CA8035B7CD9"), 1
    ),
    "area800_810_xray_fe": AreaAnalyzeClass(
        uuid.UUID("316C2EDB-E877-47C3-A94E-DA5635502A22"), 1
    ),
    "area800_810_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("E0312025-72ED-49CE-A224-E2D2BA39A5CD"), 1
    ),
    "area800_810_xray_mno": AreaAnalyzeClass(
        uuid.UUID("A6A1A012-091C-4542-82C3-0C5BFBCD4960"), 1
    ),
    "area800_810_xray_p": AreaAnalyzeClass(
        uuid.UUID("A260F830-F006-4332-B34B-6289687283D2"), 1
    ),
    "area800_810_xray_result": AreaAnalyzeClass(
        uuid.UUID("4A1AFFF3-0C62-42B4-AD1C-2EF9374E0B27"), 2
    ),
    "area800_810_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("3E875043-B330-4F1D-B958-91B90A31C393"), 1
    ),
    "area800_810_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("0B41B4D7-FE90-488A-9975-2EE3573E6481"), 1
    ),
    "area800_820_atomic_k2o": AreaAnalyzeClass(
        uuid.UUID("B2B56E8E-EE1E-42CF-AC44-2DEF841F2ED0"), 1
    ),
    "area800_820_atomic_na2o": AreaAnalyzeClass(
        uuid.UUID("44A6196B-74FB-4DFA-A061-42E198BC7E79"), 1
    ),
    "area800_820_ccs_100": AreaAnalyzeClass(
        uuid.UUID("6AE78C4A-2EEF-4DB8-8E56-5531C478DAA3"), 2
    ),
    "area800_820_ccs_150": AreaAnalyzeClass(
        uuid.UUID("1D8D41BB-5CA1-44DA-907B-FB0773BC5A87"), 2
    ),
    "area800_820_ccs_50": AreaAnalyzeClass(
        uuid.UUID("DAC42144-3252-4098-9000-2882913FB4F5"), 2
    ),
    "area800_820_ccs_avg": AreaAnalyzeClass(
        uuid.UUID("0942802F-AD8F-4B75-AEDF-82D4C93E3083"), 2
    ),
    "area800_820_ccs_description": AreaAnalyzeClass(
        uuid.UUID("19909308-C29C-4491-AB29-BAEBD40D4669"), 1
    ),
    "area800_820_ccs_input1": AreaAnalyzeClass(
        uuid.UUID("D76827B2-590B-457C-97B4-7859B687CC9C"), 1
    ),
    "area800_820_ccs_input10": AreaAnalyzeClass(
        uuid.UUID("CBB4AE0C-5BD6-4939-900E-C425967D58C1"), 1
    ),
    "area800_820_ccs_input100": AreaAnalyzeClass(
        uuid.UUID("6E9889B9-3BC3-4D92-BEBD-5AF0B166672A"), 1
    ),
    "area800_820_ccs_input11": AreaAnalyzeClass(
        uuid.UUID("36915323-F539-47F9-81D4-7E034E86FFE5"), 1
    ),
    "area800_820_ccs_input12": AreaAnalyzeClass(
        uuid.UUID("57D25597-BDF8-4692-A826-C22F0B7AB88C"), 1
    ),
    "area800_820_ccs_input13": AreaAnalyzeClass(
        uuid.UUID("F0C4818D-429D-4ADE-9314-94047EE271B7"), 1
    ),
    "area800_820_ccs_input14": AreaAnalyzeClass(
        uuid.UUID("728E0344-881B-47FF-8B21-77EBD69095F0"), 1
    ),
    "area800_820_ccs_input15": AreaAnalyzeClass(
        uuid.UUID("573A0D8F-18D4-4B1B-8E30-F2C6AB6482E1"), 1
    ),
    "area800_820_ccs_input16": AreaAnalyzeClass(
        uuid.UUID("5770D840-A265-40F4-90FC-F1A8749B7E52"), 1
    ),
    "area800_820_ccs_input17": AreaAnalyzeClass(
        uuid.UUID("55495E68-9824-4F7B-8573-470C2B237410"), 1
    ),
    "area800_820_ccs_input18": AreaAnalyzeClass(
        uuid.UUID("FE9A2AA2-2AAC-4845-8061-B23A763B926A"), 1
    ),
    "area800_820_ccs_input19": AreaAnalyzeClass(
        uuid.UUID("F92FC607-A274-4BA1-9B94-48F8A94C5C90"), 1
    ),
    "area800_820_ccs_input2": AreaAnalyzeClass(
        uuid.UUID("31DFF73B-E4E4-4F33-83F6-F50F76917FEE"), 1
    ),
    "area800_820_ccs_input20": AreaAnalyzeClass(
        uuid.UUID("4EE09069-6193-46CF-B771-3049E5934B79"), 1
    ),
    "area800_820_ccs_input21": AreaAnalyzeClass(
        uuid.UUID("7DE2D95B-DEA2-4327-9A64-F4861C169F09"), 1
    ),
    "area800_820_ccs_input22": AreaAnalyzeClass(
        uuid.UUID("6AB70916-2E72-495C-BDF7-3A3AA0D6E520"), 1
    ),
    "area800_820_ccs_input23": AreaAnalyzeClass(
        uuid.UUID("3F41465B-FA01-472E-88D1-1346E572623E"), 1
    ),
    "area800_820_ccs_input24": AreaAnalyzeClass(
        uuid.UUID("9582E034-1607-4C79-998F-73891209A96A"), 1
    ),
    "area800_820_ccs_input25": AreaAnalyzeClass(
        uuid.UUID("20A5C9F3-5E38-4464-A086-C51EF4FE9ED5"), 1
    ),
    "area800_820_ccs_input26": AreaAnalyzeClass(
        uuid.UUID("17646307-0350-4302-8370-8F04719C31BC"), 1
    ),
    "area800_820_ccs_input27": AreaAnalyzeClass(
        uuid.UUID("4546CE33-76EB-4876-A74A-24BD600B3B6F"), 1
    ),
    "area800_820_ccs_input28": AreaAnalyzeClass(
        uuid.UUID("6A7A98B2-4B58-4C9A-86F5-C6D5F8352726"), 1
    ),
    "area800_820_ccs_input29": AreaAnalyzeClass(
        uuid.UUID("587E65B7-487F-4B5F-8760-430BD45DCC74"), 1
    ),
    "area800_820_ccs_input3": AreaAnalyzeClass(
        uuid.UUID("8172F8CF-6BDA-4C2C-98CE-BF8F357A56A6"), 1
    ),
    "area800_820_ccs_input30": AreaAnalyzeClass(
        uuid.UUID("3CF3E9DE-13AF-4B78-8399-9E131A94A1BE"), 1
    ),
    "area800_820_ccs_input31": AreaAnalyzeClass(
        uuid.UUID("2A012A7D-6EE3-47F3-8302-24848E145DCA"), 1
    ),
    "area800_820_ccs_input32": AreaAnalyzeClass(
        uuid.UUID("3E353D02-8785-4748-BEF1-CAB0A30CC827"), 1
    ),
    "area800_820_ccs_input33": AreaAnalyzeClass(
        uuid.UUID("F267E4D9-C617-4D6B-82F7-2591D01CBA7F"), 1
    ),
    "area800_820_ccs_input34": AreaAnalyzeClass(
        uuid.UUID("A2458366-0A56-4695-AADB-3F094715C1CE"), 1
    ),
    "area800_820_ccs_input35": AreaAnalyzeClass(
        uuid.UUID("4DC89101-6563-46E5-AFEC-FAF512DCDD9C"), 1
    ),
    "area800_820_ccs_input36": AreaAnalyzeClass(
        uuid.UUID("4D430748-AA6B-405A-A780-4D559BE509F7"), 1
    ),
    "area800_820_ccs_input37": AreaAnalyzeClass(
        uuid.UUID("040DB931-9832-4937-9554-B7647286C1D4"), 1
    ),
    "area800_820_ccs_input38": AreaAnalyzeClass(
        uuid.UUID("DC83E2C0-97E4-4F29-ACDB-22ACFEB12E22"), 1
    ),
    "area800_820_ccs_input39": AreaAnalyzeClass(
        uuid.UUID("9D385E8A-762C-4E26-B376-691CC040790E"), 1
    ),
    "area800_820_ccs_input4": AreaAnalyzeClass(
        uuid.UUID("95B9DF9A-8EB4-462E-A666-C302496FE534"), 1
    ),
    "area800_820_ccs_input40": AreaAnalyzeClass(
        uuid.UUID("CEDC45AF-4EA5-4026-ACE4-8E942FC41F49"), 1
    ),
    "area800_820_ccs_input41": AreaAnalyzeClass(
        uuid.UUID("904A5C6E-35EF-42FB-A196-F94E572015CA"), 1
    ),
    "area800_820_ccs_input42": AreaAnalyzeClass(
        uuid.UUID("6FF88E8B-C3FE-466C-A1C7-CA522BD7C7FD"), 1
    ),
    "area800_820_ccs_input43": AreaAnalyzeClass(
        uuid.UUID("2955C74B-C2CC-4013-BED1-67E93C2C1EA2"), 1
    ),
    "area800_820_ccs_input44": AreaAnalyzeClass(
        uuid.UUID("E441D5CA-9D53-4884-B657-77734A112C49"), 1
    ),
    "area800_820_ccs_input45": AreaAnalyzeClass(
        uuid.UUID("168B0B32-0067-477D-B758-F91E18136C44"), 1
    ),
    "area800_820_ccs_input46": AreaAnalyzeClass(
        uuid.UUID("2D32B578-6AF6-4F2E-8485-FD67C0633EF1"), 1
    ),
    "area800_820_ccs_input47": AreaAnalyzeClass(
        uuid.UUID("6A0980F7-B79C-4778-B39F-816A1218837A"), 1
    ),
    "area800_820_ccs_input48": AreaAnalyzeClass(
        uuid.UUID("08E17923-5DBC-46BE-82DD-0DADF7E191AC"), 1
    ),
    "area800_820_ccs_input49": AreaAnalyzeClass(
        uuid.UUID("73F88721-BF30-46BB-8C5F-BF3992688F10"), 1
    ),
    "area800_820_ccs_input5": AreaAnalyzeClass(
        uuid.UUID("5B140A6C-4D15-47C5-85A5-8D82D3996182"), 1
    ),
    "area800_820_ccs_input50": AreaAnalyzeClass(
        uuid.UUID("0CD43367-1C03-46B3-B050-E128502AA10B"), 1
    ),
    "area800_820_ccs_input51": AreaAnalyzeClass(
        uuid.UUID("6A5767A8-9867-4EC8-9247-2E4EDDD78FE5"), 1
    ),
    "area800_820_ccs_input52": AreaAnalyzeClass(
        uuid.UUID("06F64B6A-6DEC-481D-8363-9025CD053CE4"), 1
    ),
    "area800_820_ccs_input53": AreaAnalyzeClass(
        uuid.UUID("BFC55327-7C81-4AF4-8E44-6EAD757ABCED"), 1
    ),
    "area800_820_ccs_input54": AreaAnalyzeClass(
        uuid.UUID("FA80531A-23E3-438F-B161-FBA8305C04C6"), 1
    ),
    "area800_820_ccs_input55": AreaAnalyzeClass(
        uuid.UUID("FEC1C706-AF01-4F32-ABDD-5F579CCAC73E"), 1
    ),
    "area800_820_ccs_input56": AreaAnalyzeClass(
        uuid.UUID("4F681FEB-FE1B-4D68-8029-41AF75D309F4"), 1
    ),
    "area800_820_ccs_input57": AreaAnalyzeClass(
        uuid.UUID("43AB252B-8057-4C6A-9A83-AA2FA1499F44"), 1
    ),
    "area800_820_ccs_input58": AreaAnalyzeClass(
        uuid.UUID("30735965-F190-42DB-A2DE-3EF15AD0381D"), 1
    ),
    "area800_820_ccs_input59": AreaAnalyzeClass(
        uuid.UUID("F276B13D-628A-46A3-9A38-4C8385925C26"), 1
    ),
    "area800_820_ccs_input6": AreaAnalyzeClass(
        uuid.UUID("7B0CC05E-F31C-441D-816F-65D033D8F1AF"), 1
    ),
    "area800_820_ccs_input60": AreaAnalyzeClass(
        uuid.UUID("725048BD-40CA-4D17-9BCF-76D743FCE8E3"), 1
    ),
    "area800_820_ccs_input61": AreaAnalyzeClass(
        uuid.UUID("373750C6-34B5-4D07-9FB2-AC24CF957C3C"), 1
    ),
    "area800_820_ccs_input62": AreaAnalyzeClass(
        uuid.UUID("0CD65599-9521-4C14-AE80-130D79CA2D54"), 1
    ),
    "area800_820_ccs_input63": AreaAnalyzeClass(
        uuid.UUID("042F3AEE-F36D-475F-B354-6ABF9A955E52"), 1
    ),
    "area800_820_ccs_input64": AreaAnalyzeClass(
        uuid.UUID("1381DFC1-9B13-4C56-BF1E-C5237AC0759A"), 1
    ),
    "area800_820_ccs_input65": AreaAnalyzeClass(
        uuid.UUID("C217AC4B-7585-47D7-9A20-7C129454DEED"), 1
    ),
    "area800_820_ccs_input66": AreaAnalyzeClass(
        uuid.UUID("58337ECF-30D8-4D48-A0A5-98C4B46A2D55"), 1
    ),
    "area800_820_ccs_input67": AreaAnalyzeClass(
        uuid.UUID("8C854323-5C6E-4CE1-B74C-7008519774B4"), 1
    ),
    "area800_820_ccs_input68": AreaAnalyzeClass(
        uuid.UUID("37005EC4-D02B-4CB8-A694-D1B6DAE82AD3"), 1
    ),
    "area800_820_ccs_input69": AreaAnalyzeClass(
        uuid.UUID("540248F8-B62F-4D0A-9289-3231FB0DA3CB"), 1
    ),
    "area800_820_ccs_input7": AreaAnalyzeClass(
        uuid.UUID("33C47208-E3D9-43C1-B01C-5DCEC0BA3FD5"), 1
    ),
    "area800_820_ccs_input70": AreaAnalyzeClass(
        uuid.UUID("EC143922-B65B-43F6-AADC-24D1184DF27B"), 1
    ),
    "area800_820_ccs_input71": AreaAnalyzeClass(
        uuid.UUID("9F3DDB58-E281-4A5A-8D7A-545FD37E9A1E"), 1
    ),
    "area800_820_ccs_input72": AreaAnalyzeClass(
        uuid.UUID("2A15214D-F97A-4757-88F7-7BB3BDB3DE39"), 1
    ),
    "area800_820_ccs_input73": AreaAnalyzeClass(
        uuid.UUID("C3543D50-97B0-4206-8380-EE90DDEBDAF0"), 1
    ),
    "area800_820_ccs_input74": AreaAnalyzeClass(
        uuid.UUID("161233CC-4766-450E-907F-D9C7B1B61868"), 1
    ),
    "area800_820_ccs_input75": AreaAnalyzeClass(
        uuid.UUID("98C5EA34-DB94-4130-8D5C-1C3B8BB20651"), 1
    ),
    "area800_820_ccs_input76": AreaAnalyzeClass(
        uuid.UUID("B88A5DD0-E7FB-40B8-B886-C9C24952B007"), 1
    ),
    "area800_820_ccs_input77": AreaAnalyzeClass(
        uuid.UUID("958E65DA-03D6-4E53-B047-0FF1AF532B1E"), 1
    ),
    "area800_820_ccs_input78": AreaAnalyzeClass(
        uuid.UUID("94A9FC16-2BFE-4FBF-BB14-ABBA47254D0E"), 1
    ),
    "area800_820_ccs_input79": AreaAnalyzeClass(
        uuid.UUID("FA02972A-277F-4DE9-B270-93D0ED22661D"), 1
    ),
    "area800_820_ccs_input8": AreaAnalyzeClass(
        uuid.UUID("805350F3-645F-4904-A43C-249F036AFB87"), 1
    ),
    "area800_820_ccs_input80": AreaAnalyzeClass(
        uuid.UUID("2F7705FC-C22A-4F51-ACD1-973956FB3393"), 1
    ),
    "area800_820_ccs_input81": AreaAnalyzeClass(
        uuid.UUID("BEEDEA22-9212-4497-8771-8A80C405B3ED"), 1
    ),
    "area800_820_ccs_input82": AreaAnalyzeClass(
        uuid.UUID("DFFD8D00-69B9-4D8A-9A39-327C565C4972"), 1
    ),
    "area800_820_ccs_input83": AreaAnalyzeClass(
        uuid.UUID("B5BE535C-724A-4A78-B960-655B3D32012D"), 1
    ),
    "area800_820_ccs_input84": AreaAnalyzeClass(
        uuid.UUID("A3588BEA-20EF-4710-A992-A1A780BC2605"), 1
    ),
    "area800_820_ccs_input85": AreaAnalyzeClass(
        uuid.UUID("DC6C991C-AB74-4F9B-A651-7EED3996ECFC"), 1
    ),
    "area800_820_ccs_input86": AreaAnalyzeClass(
        uuid.UUID("DD4DBBC0-9C16-439B-8DAC-37BC5DABA959"), 1
    ),
    "area800_820_ccs_input87": AreaAnalyzeClass(
        uuid.UUID("7F9F29E1-B59F-4CE2-8EE1-70FF9425031B"), 1
    ),
    "area800_820_ccs_input88": AreaAnalyzeClass(
        uuid.UUID("5A2C84B9-B5DC-4B6E-9B71-E2808DE8085B"), 1
    ),
    "area800_820_ccs_input89": AreaAnalyzeClass(
        uuid.UUID("E9AB9D93-E0F0-4962-8E78-E0D30669D01E"), 1
    ),
    "area800_820_ccs_input9": AreaAnalyzeClass(
        uuid.UUID("36E3F368-6C8F-4E48-9205-8182C720D35C"), 1
    ),
    "area800_820_ccs_input90": AreaAnalyzeClass(
        uuid.UUID("07E89DA8-9C1E-49AB-AD47-94F54061B14C"), 1
    ),
    "area800_820_ccs_input91": AreaAnalyzeClass(
        uuid.UUID("AC258954-9AC6-4C66-9230-DFA315C60C2B"), 1
    ),
    "area800_820_ccs_input92": AreaAnalyzeClass(
        uuid.UUID("A5AD78D0-D09D-48CE-9403-C2FECF77E046"), 1
    ),
    "area800_820_ccs_input93": AreaAnalyzeClass(
        uuid.UUID("EA0C3202-96D0-470D-8956-11831505B196"), 1
    ),
    "area800_820_ccs_input94": AreaAnalyzeClass(
        uuid.UUID("CB2CB5CF-8FEF-42FA-8DF6-8600AED5F617"), 1
    ),
    "area800_820_ccs_input95": AreaAnalyzeClass(
        uuid.UUID("B05AD7E3-749D-4A2B-8B9E-2E613320EDDD"), 1
    ),
    "area800_820_ccs_input96": AreaAnalyzeClass(
        uuid.UUID("D00BDE72-3112-4206-AC2B-7F905DFA8330"), 1
    ),
    "area800_820_ccs_input97": AreaAnalyzeClass(
        uuid.UUID("332645A8-1CDA-4A68-97C3-64121C5D3A50"), 1
    ),
    "area800_820_ccs_input98": AreaAnalyzeClass(
        uuid.UUID("CDFC41A1-A76C-4021-8E98-4DA3BC780436"), 1
    ),
    "area800_820_ccs_input99": AreaAnalyzeClass(
        uuid.UUID("6FFF72E0-D2DD-4A31-81E7-22481011853A"), 1
    ),
    "area800_820_ccs_std": AreaAnalyzeClass(
        uuid.UUID("0E6CE1AD-942E-4CDE-AEAD-E84B2DAE94CC"), 2
    ),
    "area800_820_description_input1": AreaAnalyzeClass(
        uuid.UUID("C7F92355-4000-435D-BABA-E3926C438551"), 1
    ),
    "area800_820_feo_avg": AreaAnalyzeClass(
        uuid.UUID("0AFBD0B2-EF2C-4ACA-A0E2-7EC2AC2C7EEE"), 2
    ),
    "area800_820_feo_input1": AreaAnalyzeClass(
        uuid.UUID("86099E27-B855-4ADC-898A-241F98BD9EDB"), 1
    ),
    "area800_820_feo_input2": AreaAnalyzeClass(
        uuid.UUID("AB99DABA-83B9-4B7C-B96B-8C86943FBA66"), 1
    ),
    "area800_820_moisture_input": AreaAnalyzeClass(
        uuid.UUID("E6551BC9-F6B4-4438-836B-AABFCD618802"), 1
    ),
    "area800_820_porosity_dry": AreaAnalyzeClass(
        uuid.UUID("58FCD543-0D5B-4996-961F-36CA0358336C"), 1
    ),
    "area800_820_porosity_result": AreaAnalyzeClass(
        uuid.UUID("568F6D75-6D8B-4EBD-8971-16AF5087955B"), 2
    ),
    "area800_820_porosity_saturated": AreaAnalyzeClass(
        uuid.UUID("43ED1F40-905F-4575-A8C0-F1B69615A888"), 1
    ),
    "area800_820_porosity_suspended": AreaAnalyzeClass(
        uuid.UUID("1255EEA8-A45E-47E3-AD02-12E7939ADAF0"), 1
    ),
    "area800_820_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("82971DC7-8D46-4C27-9263-B1F44CD0AB6F"), 1
    ),
    "area800_820_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("7449F689-18C2-4E22-9F17-4C3CDD50D22B"), 2
    ),
    "area800_820_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("4EA3ED09-FB37-4532-876C-D061435671AF"), 1
    ),
    "area800_820_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("77311961-E620-45C5-AAD7-E99B22859D9B"), 2
    ),
    "area800_820_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("2A658E8A-A665-4AA4-8354-E6A7B8DC75B9"), 1
    ),
    "area800_820_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("EB8781BF-FA06-4002-B4DD-01F0F12E6A97"), 2
    ),
    "area800_820_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("B12788AD-789F-4508-8556-EAEDD17A7C70"), 1
    ),
    "area800_820_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("7D1220B2-70FB-47E0-91AD-E108BC8E0432"), 2
    ),
    "area800_820_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("72C41925-09FD-4B87-9200-1A7B6C66FB83"), 1
    ),
    "area800_820_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("F23B249E-96F4-46F2-8332-5A85EB2D3973"), 2
    ),
    "area800_820_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("6F961CDF-B890-4405-B505-1B430AB7C012"), 1
    ),
    "area800_820_sulfur_input": AreaAnalyzeClass(
        uuid.UUID("B443F011-11B5-4C68-A67F-560E5C4A87F8"), 1
    ),
    "area800_820_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("973EC54B-8C59-4A7D-8132-4867E89DD3B1"), 2
    ),
    "area800_820_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("A8CACEAA-76C1-4DC8-B9B5-F14E4801EB02"), 1
    ),
    "area800_820_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("CA775CBA-85F9-4D58-9EBE-3384BF775039"), 1
    ),
    "area800_820_tumble_r5w": AreaAnalyzeClass(
        uuid.UUID("5D615721-6ACD-4F99-968F-9D7C5D7DAD23"), 2
    ),
    "area800_820_tumble_r63w": AreaAnalyzeClass(
        uuid.UUID("D3FF78FC-87D3-4250-9C23-15B034B2B632"), 2
    ),
    "area800_820_tumble_remain5": AreaAnalyzeClass(
        uuid.UUID("901C13BD-3C3A-4E7B-B56B-8D5CCEFC3474"), 1
    ),
    "area800_820_tumble_remain63": AreaAnalyzeClass(
        uuid.UUID("D2120FF7-D864-4B31-BA10-52E0F8DF40A4"), 1
    ),
    "area800_820_tumble_weight": AreaAnalyzeClass(
        uuid.UUID("F3F7FEC4-5EA7-49CB-BAA8-31DE3E4611C6"), 1
    ),
    "area800_820_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("C0CDB221-2EE2-4123-B2AA-844AAF55B124"), 1
    ),
    "area800_820_xray_cao": AreaAnalyzeClass(
        uuid.UUID("AA416FDC-9ED3-4D89-B312-8AA0450AD0F6"), 1
    ),
    "area800_820_xray_fe": AreaAnalyzeClass(
        uuid.UUID("1571AF95-E7C3-43AE-8304-3FD8F294FFF9"), 1
    ),
    "area800_820_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("3AB0EE72-C2F0-4470-AEBB-1031ACDCF38B"), 1
    ),
    "area800_820_xray_mno": AreaAnalyzeClass(
        uuid.UUID("C6BDDC9E-4AB7-4AA7-8176-79F3602BC896"), 1
    ),
    "area800_820_xray_p": AreaAnalyzeClass(
        uuid.UUID("4A044E91-7954-432F-8781-C9E650C61B74"), 1
    ),
    "area800_820_xray_result": AreaAnalyzeClass(
        uuid.UUID("47C68258-AAB5-4FA9-8AE2-BB1EA83116BC"), 2
    ),
    "area800_820_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("EBD26DB2-E9AB-4FC1-889F-8FB3DBCE51B4"), 1
    ),
    "area800_820_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("A9D1805C-6BFC-4D22-970F-B12E3895D09C"), 1
    ),
    "area900_910bc1_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("0E99D5B1-E12A-4FFF-998C-4A3EF7E4EAED"), 1
    ),
    "area900_910bc1_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("31609160-DD81-4712-A051-14951A009804"), 2
    ),
    "area900_910bc1_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("042043F2-A35A-4C8C-8B54-556B20DE531D"), 1
    ),
    "area900_910bc1_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("327FE11A-4BBC-47C9-9075-56412E8E69EB"), 2
    ),
    "area900_910bc1_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("06DB1B25-9087-4F29-B17A-6CB71B959C0A"), 1
    ),
    "area900_910bc1_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("649361B3-159F-4A43-8826-5A7425FEB3F6"), 2
    ),
    "area900_910bc1_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("A033404F-332F-4F03-9401-BF8081E8770C"), 1
    ),
    "area900_910bc1_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("B78E6D12-8D06-4912-8198-083DDBA3A5AB"), 2
    ),
    "area900_910bc1_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("09E32497-0971-402D-9D2F-AB9E3C98E098"), 1
    ),
    "area900_910bc1_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("E03BF00C-C71E-4BBB-9AAB-3D043AFC2AD1"), 2
    ),
    "area900_910bc1_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("033FE15F-7371-4C50-96F0-6C2B9826B6D7"), 1
    ),
    "area900_920bc2_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("B782B185-5C6B-481B-AC43-88498B99AA33"), 1
    ),
    "area900_920bc2_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("59AB2828-818A-46FE-9410-49214DD79683"), 2
    ),
    "area900_920bc2_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("BF1B53FF-202F-448A-A3EF-B7B5D9568EDB"), 1
    ),
    "area900_920bc2_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("A1C4D4B0-A3EC-4DA7-AE46-9680AF32425C"), 2
    ),
    "area900_920bc2_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("7CA58608-BB52-4874-99F7-914C775EFDE7"), 1
    ),
    "area900_920bc2_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("0B98C18C-C587-4409-8C93-9EC10327572B"), 2
    ),
    "area900_920bc2_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("7CD299E5-D93F-4BBA-A96C-D73541AB7DE9"), 1
    ),
    "area900_920bc2_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("95694758-4DCA-4C61-8BB5-836E56647224"), 2
    ),
    "area900_920bc2_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("81734D68-AF04-4C4A-A3FC-BD4AE072C638"), 1
    ),
    "area900_920bc2_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("8FE17A89-989E-4347-AE5F-73F461CE00EA"), 2
    ),
    "area900_920bc2_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("330F3BEB-FB37-4CAA-AFF3-37D6ED738C11"), 1
    ),
    "area900_ballmill_blaine_b": AreaAnalyzeClass(
        uuid.UUID("214C267C-E20C-4B07-9EB7-16DAD846403A"), 1
    ),
    "area900_ballmill_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("DBD1338B-E34F-43F5-BE44-2ACCE439169F"), 1
    ),
    "area900_ballmill_blaine_e": AreaAnalyzeClass(
        uuid.UUID("8B69885F-75E3-4593-A94D-708C5BC90C27"), 1
    ),
    "area900_ballmill_blaine_es": AreaAnalyzeClass(
        uuid.UUID("ABCC74BE-F2F0-47ED-A9D2-042ABF2C6217"), 1
    ),
    "area900_ballmill_blaine_p": AreaAnalyzeClass(
        uuid.UUID("41403187-C853-4219-8CDE-B6B3B9FF49C0"), 1
    ),
    "area900_ballmill_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("A21BA197-EFB8-4761-909D-C2632BC1DEE1"), 1
    ),
    "area900_ballmill_blaine_result": AreaAnalyzeClass(
        uuid.UUID("CCF33870-8224-42F8-A730-2819C7F62FC2"), 2
    ),
    "area900_ballmill_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("1287D324-4430-466F-8064-07CDE874F383"), 1
    ),
    "area900_ballmill_blaine_t": AreaAnalyzeClass(
        uuid.UUID("63726EC5-941D-42E6-A707-C7567E41094D"), 1
    ),
    "area900_ballmill_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("EBF6EE76-2F48-4EFA-B6F3-1A7CCE441A93"), 1
    ),
    "area900_ballmill_density_input": AreaAnalyzeClass(
        uuid.UUID("E18FBC44-EA0A-4C73-A507-32864A88076D"), 1
    ),
    "area900_clarifier_blaine_b": AreaAnalyzeClass(
        uuid.UUID("66AA82AB-3A22-4155-9558-12C5A43A3D2A"), 1
    ),
    "area900_clarifier_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("7903B44A-3BD7-4FE3-BAC4-0CE7AC70AB00"), 1
    ),
    "area900_clarifier_blaine_e": AreaAnalyzeClass(
        uuid.UUID("08F72F75-8B30-4D89-AAAC-0EA4989785EF"), 1
    ),
    "area900_clarifier_blaine_es": AreaAnalyzeClass(
        uuid.UUID("8F5AB342-1336-4BAC-B406-EC82659E9E96"), 1
    ),
    "area900_clarifier_blaine_p": AreaAnalyzeClass(
        uuid.UUID("A989EFEE-3EED-44A9-AB59-DFB678E52446"), 1
    ),
    "area900_clarifier_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("E2F374F0-B17F-4375-A472-8715F2CB6E64"), 1
    ),
    "area900_clarifier_blaine_result": AreaAnalyzeClass(
        uuid.UUID("2817863B-6053-47FF-AB1F-12E115DB7144"), 2
    ),
    "area900_clarifier_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("75BB23C2-8650-4014-B5CC-B7DD210E323D"), 1
    ),
    "area900_clarifier_blaine_t": AreaAnalyzeClass(
        uuid.UUID("984055EB-153B-43CF-A540-03F4BF5A1DFD"), 1
    ),
    "area900_clarifier_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("0FD9CB72-B294-44A5-9C3D-BDB8710C1551"), 1
    ),
    "area900_clarifier_density_input": AreaAnalyzeClass(
        uuid.UUID("EA0CA49D-AC04-4726-9F91-71C4A21F8F01"), 1
    ),
    "area900_filtercake_blaine_b": AreaAnalyzeClass(
        uuid.UUID("71992B48-52F2-476E-A356-8F6704AAE179"), 1
    ),
    "area900_filtercake_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("81379BA9-C55C-4318-BFFB-A3DFE8A89DED"), 1
    ),
    "area900_filtercake_blaine_e": AreaAnalyzeClass(
        uuid.UUID("CD295BE1-9641-45B2-92A2-971AC622F124"), 1
    ),
    "area900_filtercake_blaine_es": AreaAnalyzeClass(
        uuid.UUID("B0BC8E22-2B01-454D-B72E-F55331B2B279"), 1
    ),
    "area900_filtercake_blaine_p": AreaAnalyzeClass(
        uuid.UUID("9F8AB5F9-8827-49C9-AB09-6CF46890ABC8"), 1
    ),
    "area900_filtercake_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("7453F26D-5C17-45CD-BA99-34462C9F6096"), 1
    ),
    "area900_filtercake_blaine_result": AreaAnalyzeClass(
        uuid.UUID("FDCC4B2B-3319-4914-9C96-5167AB7F4E42"), 2
    ),
    "area900_filtercake_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("0BB3597E-FF88-4200-A7FC-CC38920B899A"), 1
    ),
    "area900_filtercake_blaine_t": AreaAnalyzeClass(
        uuid.UUID("DC5BAF38-7E7D-4928-B49C-BEBA9F8D47C1"), 1
    ),
    "area900_filtercake_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("805E7F46-71F9-44B9-87D9-D5C7F685508E"), 1
    ),
    "area900_filtercake_moisture_input": AreaAnalyzeClass(
        uuid.UUID("17381F9C-16FD-40E1-925A-E6C65B896BA1"), 1
    ),
    "area900_slurry_blaine_b": AreaAnalyzeClass(
        uuid.UUID("D24263A8-7C4A-4433-ABDE-9714913A7A30"), 1
    ),
    "area900_slurry_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("EC1B9B68-C2BD-425B-A8D7-6B8AA5B64FA4"), 1
    ),
    "area900_slurry_blaine_e": AreaAnalyzeClass(
        uuid.UUID("715F47F0-270D-4C18-A9C1-6285454A2EC8"), 1
    ),
    "area900_slurry_blaine_es": AreaAnalyzeClass(
        uuid.UUID("587BA747-63C5-4936-B2A2-BA3495D40D88"), 1
    ),
    "area900_slurry_blaine_p": AreaAnalyzeClass(
        uuid.UUID("6A2C4ED8-A848-4296-B9A2-BA163AA4A109"), 1
    ),
    "area900_slurry_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("31101CA8-3ED4-49D0-A53F-0BBF34725885"), 1
    ),
    "area900_slurry_blaine_result": AreaAnalyzeClass(
        uuid.UUID("87ED6167-F3C3-4D38-8F57-3150B7BFE696"), 2
    ),
    "area900_slurry_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("94EEBF9D-F04F-45B9-8C07-5F64AFFBF0D9"), 1
    ),
    "area900_slurry_blaine_t": AreaAnalyzeClass(
        uuid.UUID("7628AE4F-1650-4724-95C3-3D3596AE367E"), 1
    ),
    "area900_slurry_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("E5455C57-C4EA-4B93-BE26-D47CB3805357"), 1
    ),
    "area900_slurry_density_input": AreaAnalyzeClass(
        uuid.UUID("BEDDE64A-CE08-46DA-B1F7-254D39E6A7F0"), 1
    ),
    "area900_thickener_blaine_b": AreaAnalyzeClass(
        uuid.UUID("68836338-823F-49B7-844E-EEF46E03AC8B"), 1
    ),
    "area900_thickener_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("CAB37555-BF9E-44A3-8233-3BA9D477A095"), 1
    ),
    "area900_thickener_blaine_e": AreaAnalyzeClass(
        uuid.UUID("551610DF-CA0F-4A16-BF67-FA5DDDEA0B5C"), 1
    ),
    "area900_thickener_blaine_es": AreaAnalyzeClass(
        uuid.UUID("C350C85B-9D45-4579-90F0-12407E566FCA"), 1
    ),
    "area900_thickener_blaine_p": AreaAnalyzeClass(
        uuid.UUID("647E71D9-9F90-491C-872C-FC312FCF298A"), 1
    ),
    "area900_thickener_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("2359C90F-A925-460D-8B97-5AF0478A5B45"), 1
    ),
    "area900_thickener_blaine_result": AreaAnalyzeClass(
        uuid.UUID("6EE52BA2-835D-4CA0-A0BC-00750845006D"), 2
    ),
    "area900_thickener_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("A396A9BE-2F53-4225-8F25-C8C979A073EA"), 1
    ),
    "area900_thickener_blaine_t": AreaAnalyzeClass(
        uuid.UUID("FF714CB7-59A0-41A8-BC45-9E10152760E2"), 1
    ),
    "area900_thickener_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("D6DCD8C7-B730-44EB-B091-F45453BA4E00"), 1
    ),
    "area900_thickener_density_input": AreaAnalyzeClass(
        uuid.UUID("7CB1A6E1-D464-466E-BC9F-1B0CAA58206A"), 1
    ),
    "chunk_chunk_feo_avg": AreaAnalyzeClass(
        uuid.UUID("E5E07CCD-2AC5-4B76-A309-D5585255B6B3"), 2
    ),
    "chunk_chunk_feo_input1": AreaAnalyzeClass(
        uuid.UUID("FCF169B4-C3DC-444C-A829-9382C6A2AB7F"), 1
    ),
    "chunk_chunk_feo_input2": AreaAnalyzeClass(
        uuid.UUID("86164391-A123-4C98-B31E-AEB1A32A35D5"), 1
    ),
    "chunk_chunk_moisture_input": AreaAnalyzeClass(
        uuid.UUID("06711C68-AA51-44DF-BB12-7362E45CBBB3"), 1
    ),
    "chunk_chunk_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("B46E7014-7F33-4CD7-8B54-F7425F265AB5"), 1
    ),
    "chunk_chunk_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("45921446-1029-4328-92DA-2A160D1E0142"), 2
    ),
    "chunk_chunk_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("62B434D0-4A93-483C-92BD-211ECAC4EF93"), 1
    ),
    "chunk_chunk_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("699BBEA1-D871-4613-98D5-D633AD8AEDA5"), 2
    ),
    "chunk_chunk_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("6BF3D329-4DF2-404E-A915-E068FF7DCEAC"), 1
    ),
    "chunk_chunk_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("DD9231C2-EDE6-4CD6-94F3-5E429659B278"), 2
    ),
    "chunk_chunk_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("925A82F4-31B3-4304-AC5D-3545F021EA25"), 1
    ),
    "chunk_chunk_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("BDA6D73D-BD62-4634-AF86-EC60926143A4"), 2
    ),
    "chunk_chunk_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("8714DDA8-AD5B-482A-903C-F0CB953CF156"), 1
    ),
    "chunk_chunk_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("CB98E6B4-CB5B-484C-86B3-0E2EE61D8BC6"), 2
    ),
    "chunk_chunk_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("4431FC5C-0913-44B8-8326-150B26C4409C"), 1
    ),
    "chunk_chunk_sulfur_input": AreaAnalyzeClass(
        uuid.UUID("A536D56E-C42D-4227-846E-32568A2B250C"), 1
    ),
    "chunk_chunk_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("35031E4D-B5BE-4BC8-A248-A01120E819A4"), 2
    ),
    "chunk_chunk_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("C29A63E7-CE00-46AA-AA13-1329F67EE341"), 1
    ),
    "chunk_chunk_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("A0304167-4F3B-428D-A9AA-206E233BFF8E"), 1
    ),
    "chunk_chunk_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("60326116-5BCF-456A-9049-55A206DAB760"), 1
    ),
    "chunk_chunk_xray_cao": AreaAnalyzeClass(
        uuid.UUID("FB2746DB-9163-4AFC-A2C9-980ECCF44938"), 1
    ),
    "chunk_chunk_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("1A8A9E63-E5B3-4737-B2F3-4634CD94F6CE"), 1
    ),
    "chunk_chunk_xray_mno": AreaAnalyzeClass(
        uuid.UUID("7472D652-C292-4924-AA46-8A29D03A19AF"), 1
    ),
    "chunk_chunk_xray_p": AreaAnalyzeClass(
        uuid.UUID("80CF2672-DB43-45BB-BD53-83AF24DA04C2"), 1
    ),
    "chunk_chunk_xray_result": AreaAnalyzeClass(
        uuid.UUID("B4D407D1-5858-4DCE-A751-AAACCAF6EF27"), 2
    ),
    "chunk_chunk_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("DE9FB1A5-04C8-4290-AE58-7EFAB01458FB"), 1
    ),
    "chunk_chunk_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("6EA30BD5-D55C-4636-9CAC-59EC5B2BDD26"), 1
    ),
    "disc_disc1_drop_avg": AreaAnalyzeClass(
        uuid.UUID("602F17D4-7419-4504-8756-FB651804A64D"), 2
    ),
    "disc_disc1_drop_input1 ": AreaAnalyzeClass(
        uuid.UUID("98BDD5BA-42E9-419A-97C7-A411CF88A701"), 1
    ),
    "disc_disc1_drop_input10": AreaAnalyzeClass(
        uuid.UUID("010A263F-88C3-4C30-B626-818E6588D2B4"), 1
    ),
    "disc_disc1_drop_input11": AreaAnalyzeClass(
        uuid.UUID("7C2B28AE-E7B5-4B16-A8FE-8FB340C60786"), 1
    ),
    "disc_disc1_drop_input12": AreaAnalyzeClass(
        uuid.UUID("7C1F72CF-BD73-46BF-892F-D7F9364D6EF1"), 1
    ),
    "disc_disc1_drop_input2 ": AreaAnalyzeClass(
        uuid.UUID("810C18CC-A841-4572-B28A-4B280844F043"), 1
    ),
    "disc_disc1_drop_input3 ": AreaAnalyzeClass(
        uuid.UUID("24671373-61C3-4250-903B-51D0D3774CD8"), 1
    ),
    "disc_disc1_drop_input4 ": AreaAnalyzeClass(
        uuid.UUID("B24112B0-086D-47D4-9CC4-CE38308150F1"), 1
    ),
    "disc_disc1_drop_input5": AreaAnalyzeClass(
        uuid.UUID("64A06E3B-7AAA-4108-BB88-380A7AA7F93B"), 1
    ),
    "disc_disc1_drop_input6 ": AreaAnalyzeClass(
        uuid.UUID("5EB16309-7CE0-4081-A024-A48C23B20C60"), 1
    ),
    "disc_disc1_drop_input7 ": AreaAnalyzeClass(
        uuid.UUID("D79499C7-AD15-4815-860E-38D3E800426A"), 1
    ),
    "disc_disc1_drop_input8 ": AreaAnalyzeClass(
        uuid.UUID("91C3F6D4-B2F6-4251-848D-0469656A2FCE"), 1
    ),
    "disc_disc1_drop_input9 ": AreaAnalyzeClass(
        uuid.UUID("40840BE4-9A24-4A8A-B9C8-C54C8F03DCE4"), 1
    ),
    "disc_disc1_drop_std": AreaAnalyzeClass(
        uuid.UUID("A1587617-1884-49A4-A359-B152AF9A5EE8"), 2
    ),
    "disc_disc1_gcs_avg": AreaAnalyzeClass(
        uuid.UUID("B5ABD4BD-3C13-4921-B0B6-5267FDAD6BF2"), 2
    ),
    "disc_disc1_gcs_input1 ": AreaAnalyzeClass(
        uuid.UUID("D1B271A1-0A88-4A25-8E22-8A9238E2D605"), 1
    ),
    "disc_disc1_gcs_input10": AreaAnalyzeClass(
        uuid.UUID("2A03EC34-4909-47F0-8131-E28EF9040E2B"), 1
    ),
    "disc_disc1_gcs_input11": AreaAnalyzeClass(
        uuid.UUID("E99485E8-1DCB-471F-AE2E-C2C3A5596F58"), 1
    ),
    "disc_disc1_gcs_input12": AreaAnalyzeClass(
        uuid.UUID("0E3FD6F4-B6AF-40E0-9474-833745725EF6"), 1
    ),
    "disc_disc1_gcs_input2 ": AreaAnalyzeClass(
        uuid.UUID("BBE482DB-9C71-4DB8-9307-E0107D55F842"), 1
    ),
    "disc_disc1_gcs_input3 ": AreaAnalyzeClass(
        uuid.UUID("989AB130-290E-4677-A912-98662563577C"), 1
    ),
    "disc_disc1_gcs_input4 ": AreaAnalyzeClass(
        uuid.UUID("FD941912-D975-46E4-A548-7365FA559E38"), 1
    ),
    "disc_disc1_gcs_input5 ": AreaAnalyzeClass(
        uuid.UUID("99B81D3E-791F-4F9C-B247-809CB928EC31"), 1
    ),
    "disc_disc1_gcs_input6 ": AreaAnalyzeClass(
        uuid.UUID("9B3FDFAA-0A2D-4ED1-B5F7-3FE570B63A71"), 1
    ),
    "disc_disc1_gcs_input7 ": AreaAnalyzeClass(
        uuid.UUID("999B9D2D-D677-435E-9C62-EB711C87508E"), 1
    ),
    "disc_disc1_gcs_input8 ": AreaAnalyzeClass(
        uuid.UUID("A9490228-E089-4B06-B9C8-7E85EF0D0889"), 1
    ),
    "disc_disc1_gcs_input9 ": AreaAnalyzeClass(
        uuid.UUID("BD1D0693-F3E9-4AF7-9B11-0E1810FC2AC8"), 1
    ),
    "disc_disc1_gcs_std": AreaAnalyzeClass(
        uuid.UUID("A3147F41-498A-4D8D-B95D-8634324B3B70"), 2
    ),
    "disc_disc1_moisture_input": AreaAnalyzeClass(
        uuid.UUID("1F55C2C9-4446-42D0-9BCD-EC62FEFEF31A"), 1
    ),
    "disc_disc1_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("D9622875-06B9-47A3-AF5A-334A94885983"), 1
    ),
    "disc_disc1_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("108C82F2-5266-44AE-A2FF-FDC77BB77B9E"), 2
    ),
    "disc_disc1_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("C1AADC8B-597F-476C-8739-64B3052E81A6"), 1
    ),
    "disc_disc1_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("B0F6BC46-4B52-4364-A33B-6877CCA7617A"), 2
    ),
    "disc_disc1_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("87DD3642-D2AD-4CBE-811B-B0C7BD5A8353"), 1
    ),
    "disc_disc1_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("9A537946-D4D6-4017-A150-973D6C565252"), 2
    ),
    "disc_disc1_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("01A0FB6A-FEC9-451D-A7A5-0ED9ADD0C1E9"), 1
    ),
    "disc_disc1_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("B05E9802-ED3E-49A1-9473-4C3624CBB6A5"), 2
    ),
    "disc_disc1_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("D726B3AF-204C-4FB1-8022-A679050DAE7D"), 1
    ),
    "disc_disc1_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("DA512C5E-4E1F-4AB4-81B8-CE756961C2F2"), 2
    ),
    "disc_disc1_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("1E283F5E-F9D4-4341-BFA7-440F7D30B504"), 1
    ),
    "disc_disc2_drop_avg": AreaAnalyzeClass(
        uuid.UUID("41ACFEE2-4668-4CDB-A1B3-FA90264C80E3"), 2
    ),
    "disc_disc2_drop_input1 ": AreaAnalyzeClass(
        uuid.UUID("CC4AE9D2-6DEF-401F-8B8B-959C50705205"), 1
    ),
    "disc_disc2_drop_input10": AreaAnalyzeClass(
        uuid.UUID("54F9B5DA-0047-4019-A8E9-A2C277A9AA7A"), 1
    ),
    "disc_disc2_drop_input11": AreaAnalyzeClass(
        uuid.UUID("D2DD5B3E-DA18-4E0F-8804-1E6CB03B686F"), 1
    ),
    "disc_disc2_drop_input12": AreaAnalyzeClass(
        uuid.UUID("C59A865D-19FA-4E85-9409-B66ACF219CCC"), 1
    ),
    "disc_disc2_drop_input2 ": AreaAnalyzeClass(
        uuid.UUID("AC4439B9-C9D2-40F3-AA9D-976F601A1690"), 1
    ),
    "disc_disc2_drop_input3 ": AreaAnalyzeClass(
        uuid.UUID("9279329E-34D2-4F1B-A3D9-B2B831EBC141"), 1
    ),
    "disc_disc2_drop_input4 ": AreaAnalyzeClass(
        uuid.UUID("ED6921DA-6816-4BA0-A2AE-7159C7F7F35A"), 1
    ),
    "disc_disc2_drop_input5": AreaAnalyzeClass(
        uuid.UUID("E1D06CF1-C690-4DB0-8757-7F86903420EA"), 1
    ),
    "disc_disc2_drop_input6 ": AreaAnalyzeClass(
        uuid.UUID("CB73ECF5-EE57-4D7C-9388-FB2E8901156F"), 1
    ),
    "disc_disc2_drop_input7 ": AreaAnalyzeClass(
        uuid.UUID("1E6220EA-FE24-4879-A475-737199AA9F31"), 1
    ),
    "disc_disc2_drop_input8 ": AreaAnalyzeClass(
        uuid.UUID("CCC23700-57A5-4918-9855-061007C6559C"), 1
    ),
    "disc_disc2_drop_input9 ": AreaAnalyzeClass(
        uuid.UUID("443E00D6-0395-4698-B375-A6513FFE1895"), 1
    ),
    "disc_disc2_drop_std": AreaAnalyzeClass(
        uuid.UUID("7567D3C4-CB8D-4C78-BCC3-C7CCBE1DCD6A"), 2
    ),
    "disc_disc2_gcs_avg": AreaAnalyzeClass(
        uuid.UUID("CEA3E794-6B3C-4575-BD4A-BB6FF21690C6"), 2
    ),
    "disc_disc2_gcs_input1 ": AreaAnalyzeClass(
        uuid.UUID("84162CDB-A972-4231-88E6-A9A3A321E99C"), 1
    ),
    "disc_disc2_gcs_input10": AreaAnalyzeClass(
        uuid.UUID("521549F7-C579-4419-9C38-71E88BA67571"), 1
    ),
    "disc_disc2_gcs_input11": AreaAnalyzeClass(
        uuid.UUID("4480E4DE-1798-4E7D-8AB4-A8314BA27975"), 1
    ),
    "disc_disc2_gcs_input12": AreaAnalyzeClass(
        uuid.UUID("B196AD1F-32D9-4439-9D41-401EF1B9A7A0"), 1
    ),
    "disc_disc2_gcs_input2 ": AreaAnalyzeClass(
        uuid.UUID("41EC9520-574B-454E-9564-FA5D75B93B39"), 1
    ),
    "disc_disc2_gcs_input3 ": AreaAnalyzeClass(
        uuid.UUID("4CA3CA1D-7ECF-4571-907D-80B5AA7E18B3"), 1
    ),
    "disc_disc2_gcs_input4 ": AreaAnalyzeClass(
        uuid.UUID("50077147-CD80-4156-9F34-248BD19DD768"), 1
    ),
    "disc_disc2_gcs_input5 ": AreaAnalyzeClass(
        uuid.UUID("0B7926B8-6C9C-49F2-B1E9-B682598CE443"), 1
    ),
    "disc_disc2_gcs_input6 ": AreaAnalyzeClass(
        uuid.UUID("27A28641-1E0C-4D8E-B930-E316EFCFF0DD"), 1
    ),
    "disc_disc2_gcs_input7 ": AreaAnalyzeClass(
        uuid.UUID("0C0E45F8-C86F-4CBC-B051-B4391F2BB082"), 1
    ),
    "disc_disc2_gcs_input8 ": AreaAnalyzeClass(
        uuid.UUID("50FCF4E5-925C-4EC1-BF31-0EA755A8EFE6"), 1
    ),
    "disc_disc2_gcs_input9 ": AreaAnalyzeClass(
        uuid.UUID("2B2A1916-CF3C-4206-91B6-4971FA8FE75E"), 1
    ),
    "disc_disc2_gcs_std": AreaAnalyzeClass(
        uuid.UUID("E540B5D2-5A6B-4D5B-BB64-AB9C14840C6B"), 2
    ),
    "disc_disc2_moisture_input": AreaAnalyzeClass(
        uuid.UUID("1588C378-6725-4614-A123-EFA0619F5CDB"), 1
    ),
    "disc_disc2_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("A8429596-ED4B-4677-85E0-D6044420D2FB"), 1
    ),
    "disc_disc2_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("7B578538-897B-420F-98EF-B71AD0BC91CD"), 2
    ),
    "disc_disc2_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("A81A4605-C5C6-42E5-9006-80B14DB98FDF"), 1
    ),
    "disc_disc2_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("861CFB3C-EEF7-4416-81A5-98038464BBFA"), 2
    ),
    "disc_disc2_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("F55899B7-1A4A-42A7-881D-C64B9E2EBCF5"), 1
    ),
    "disc_disc2_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("D735A6B9-8B03-4B69-A5E8-3559D46D01C2"), 2
    ),
    "disc_disc2_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("78D00D42-68E6-47A6-A9AF-5EB284AB5B13"), 1
    ),
    "disc_disc2_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("D108EBD6-ACD9-4833-A52B-A479CAD4D8F3"), 2
    ),
    "disc_disc2_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("CD919ABB-FD13-4C50-B9DC-7515D2760998"), 1
    ),
    "disc_disc2_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("50B7E5F4-008F-41BF-B357-ADC4288E8D69"), 2
    ),
    "disc_disc2_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("7C83A01F-7018-4C2E-8B2C-DE3BCA145B31"), 1
    ),
    "disc_disc3_drop_avg": AreaAnalyzeClass(
        uuid.UUID("5E5867FC-E521-4FFB-B09A-DB52C00C047C"), 2
    ),
    "disc_disc3_drop_input1 ": AreaAnalyzeClass(
        uuid.UUID("A0FF2E4B-7D00-40B5-B811-EC94D60AFD69"), 1
    ),
    "disc_disc3_drop_input10": AreaAnalyzeClass(
        uuid.UUID("F851BAA5-E8E3-432A-AC65-85FA75C76344"), 1
    ),
    "disc_disc3_drop_input11": AreaAnalyzeClass(
        uuid.UUID("54E67ACC-4532-47DB-8091-C357BA903C14"), 1
    ),
    "disc_disc3_drop_input12": AreaAnalyzeClass(
        uuid.UUID("EE1D066C-A884-4FBA-B245-F005093322AC"), 1
    ),
    "disc_disc3_drop_input2 ": AreaAnalyzeClass(
        uuid.UUID("87D68D51-3FF1-42C0-AD9A-E3D083DF84B0"), 1
    ),
    "disc_disc3_drop_input3 ": AreaAnalyzeClass(
        uuid.UUID("7AED5115-AA6E-4670-BC81-06E37EAE72F0"), 1
    ),
    "disc_disc3_drop_input4 ": AreaAnalyzeClass(
        uuid.UUID("787B7EFC-597F-4D1C-A5C5-798EF7CC6802"), 1
    ),
    "disc_disc3_drop_input5": AreaAnalyzeClass(
        uuid.UUID("827A8A1C-7E00-481B-BE41-76E82FC95B3D"), 1
    ),
    "disc_disc3_drop_input6 ": AreaAnalyzeClass(
        uuid.UUID("67F07A33-6997-4850-AF9C-2CF998AEB54D"), 1
    ),
    "disc_disc3_drop_input7 ": AreaAnalyzeClass(
        uuid.UUID("EC9FE6D1-CBEA-4288-86BF-6726DC7CDD2B"), 1
    ),
    "disc_disc3_drop_input8 ": AreaAnalyzeClass(
        uuid.UUID("3C9E6C91-B9F6-47AC-A97E-6A25CF540FAF"), 1
    ),
    "disc_disc3_drop_input9 ": AreaAnalyzeClass(
        uuid.UUID("85EE3E7C-10E9-4D91-8AA9-E66AEF30DE8C"), 1
    ),
    "disc_disc3_drop_std": AreaAnalyzeClass(
        uuid.UUID("8FB96E67-F1A9-4787-9395-85C88732F918"), 2
    ),
    "disc_disc3_gcs_avg": AreaAnalyzeClass(
        uuid.UUID("31CC45AE-CC1D-4CA9-A805-412FD4932F0B"), 2
    ),
    "disc_disc3_gcs_input1 ": AreaAnalyzeClass(
        uuid.UUID("963AD27F-BF5D-4EA1-9189-11AB7F3C9DDD"), 1
    ),
    "disc_disc3_gcs_input10": AreaAnalyzeClass(
        uuid.UUID("6C107C85-9886-4C81-8D1C-83319C92DE51"), 1
    ),
    "disc_disc3_gcs_input11": AreaAnalyzeClass(
        uuid.UUID("A4C3C99F-AFC6-48E8-8251-77A33AAEDB3B"), 1
    ),
    "disc_disc3_gcs_input12": AreaAnalyzeClass(
        uuid.UUID("5C370FA9-6B8F-4827-9964-6B038BE99258"), 1
    ),
    "disc_disc3_gcs_input2 ": AreaAnalyzeClass(
        uuid.UUID("37B689B8-E772-4490-9C10-825A1F42CB2B"), 1
    ),
    "disc_disc3_gcs_input3 ": AreaAnalyzeClass(
        uuid.UUID("EA636D59-AE1D-4AC6-BDD6-01B471B7100A"), 1
    ),
    "disc_disc3_gcs_input4 ": AreaAnalyzeClass(
        uuid.UUID("41A48986-2804-424D-A835-2DD0B0E0A10A"), 1
    ),
    "disc_disc3_gcs_input5 ": AreaAnalyzeClass(
        uuid.UUID("B1209F80-42F3-49B2-8C16-705E980234AA"), 1
    ),
    "disc_disc3_gcs_input6 ": AreaAnalyzeClass(
        uuid.UUID("89298ACF-1A1D-40E1-B152-DB2CF5DD8618"), 1
    ),
    "disc_disc3_gcs_input7 ": AreaAnalyzeClass(
        uuid.UUID("9108BF25-5A15-4EA4-AC87-BFB4705EC243"), 1
    ),
    "disc_disc3_gcs_input8 ": AreaAnalyzeClass(
        uuid.UUID("B1F0879B-5C65-4639-A9D4-1CAA9EA160CA"), 1
    ),
    "disc_disc3_gcs_input9 ": AreaAnalyzeClass(
        uuid.UUID("516CE3DA-BCFD-462D-94A4-D4CD0955653E"), 1
    ),
    "disc_disc3_gcs_std": AreaAnalyzeClass(
        uuid.UUID("067F73CA-9441-43C9-B818-F62C91314B6F"), 2
    ),
    "disc_disc3_moisture_input": AreaAnalyzeClass(
        uuid.UUID("8C95D336-D747-4FC1-A060-B9DFAAB0695C"), 1
    ),
    "disc_disc3_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("B9985AFE-3FDB-4ED9-B9FA-9A14E72EC94B"), 1
    ),
    "disc_disc3_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("33328523-92DC-4510-92FE-8997B2FF80EF"), 2
    ),
    "disc_disc3_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("14BCF4E6-BD0E-4DA2-8A39-97EB9F33D7F4"), 1
    ),
    "disc_disc3_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("3E3C9389-68E7-44EA-8811-75E4049087A7"), 2
    ),
    "disc_disc3_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("EAAB36DE-DE6A-4BA2-9E6E-7A23CE8443DE"), 1
    ),
    "disc_disc3_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("DD7FA55B-1712-4689-8FA3-732771B215DC"), 2
    ),
    "disc_disc3_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("A3F665B4-B41B-42CC-B15D-E3DDEF98EB5A"), 1
    ),
    "disc_disc3_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("36C030D5-EE15-49F0-B79D-7495963DE82D"), 2
    ),
    "disc_disc3_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("0298BB48-A2C4-45CA-9AB0-10C3FBDA5951"), 1
    ),
    "disc_disc3_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("3C4CAB29-12D2-4463-BEC1-409C5226ACB9"), 2
    ),
    "disc_disc3_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("5BE09990-B446-41E6-BDAC-67CB515FB54C"), 1
    ),
    "disc_disc4_drop_avg": AreaAnalyzeClass(
        uuid.UUID("D8AE5D1C-C018-48CB-8080-32D4C5EECB81"), 2
    ),
    "disc_disc4_drop_input1 ": AreaAnalyzeClass(
        uuid.UUID("71C941AA-1E80-48A9-87BD-B8719AAA6DAA"), 1
    ),
    "disc_disc4_drop_input10": AreaAnalyzeClass(
        uuid.UUID("895B8447-4157-4302-964F-B37EEE138B0E"), 1
    ),
    "disc_disc4_drop_input11": AreaAnalyzeClass(
        uuid.UUID("3EECE08C-C998-4F76-A794-8CDD775508F0"), 1
    ),
    "disc_disc4_drop_input12": AreaAnalyzeClass(
        uuid.UUID("5FB9747E-EBC2-4546-BD0D-EA570D5E777D"), 1
    ),
    "disc_disc4_drop_input2 ": AreaAnalyzeClass(
        uuid.UUID("04C73313-C31C-4D29-BEF0-C693D2C22944"), 1
    ),
    "disc_disc4_drop_input3 ": AreaAnalyzeClass(
        uuid.UUID("25B8C8DD-5236-40A4-B1D5-C39D71120988"), 1
    ),
    "disc_disc4_drop_input4 ": AreaAnalyzeClass(
        uuid.UUID("3DD4D3AF-7472-46C8-BCA0-CD1C5112E901"), 1
    ),
    "disc_disc4_drop_input5": AreaAnalyzeClass(
        uuid.UUID("9CC9439F-EB89-4449-9E95-333500169C02"), 1
    ),
    "disc_disc4_drop_input6 ": AreaAnalyzeClass(
        uuid.UUID("82E41A95-299A-4647-8BE6-8CAC7C3DC9C5"), 1
    ),
    "disc_disc4_drop_input7 ": AreaAnalyzeClass(
        uuid.UUID("9A3011B7-A73F-4CBA-9863-3D7FF2F7DE0A"), 1
    ),
    "disc_disc4_drop_input8 ": AreaAnalyzeClass(
        uuid.UUID("49414821-AD3F-4A97-B538-5BF7EE34AA3C"), 1
    ),
    "disc_disc4_drop_input9 ": AreaAnalyzeClass(
        uuid.UUID("B10956F4-A1E2-4207-89C1-8A700B5B3A2C"), 1
    ),
    "disc_disc4_drop_std": AreaAnalyzeClass(
        uuid.UUID("8811A3CB-C6A5-4165-9877-92EDBC22FD64"), 2
    ),
    "disc_disc4_gcs_avg": AreaAnalyzeClass(
        uuid.UUID("5CA65A7B-A403-42E2-B624-6EE0BC02AD78"), 2
    ),
    "disc_disc4_gcs_input1 ": AreaAnalyzeClass(
        uuid.UUID("53F4CF96-1405-4783-BBC5-3E514F6B96F7"), 1
    ),
    "disc_disc4_gcs_input10": AreaAnalyzeClass(
        uuid.UUID("2EDE781B-2247-4A99-BEA4-B6D60EAB0C43"), 1
    ),
    "disc_disc4_gcs_input11": AreaAnalyzeClass(
        uuid.UUID("3899B91E-CD17-4D8D-AD9B-D1FD3477EBA2"), 1
    ),
    "disc_disc4_gcs_input12": AreaAnalyzeClass(
        uuid.UUID("41F90A9A-9CC6-426C-856B-CA9C51D26B30"), 1
    ),
    "disc_disc4_gcs_input2 ": AreaAnalyzeClass(
        uuid.UUID("FC2ABBB4-DA3C-4063-9E7E-DC1A76AE8158"), 1
    ),
    "disc_disc4_gcs_input3 ": AreaAnalyzeClass(
        uuid.UUID("B5B80F7A-F1C6-4D2F-AF52-7F2389FCB857"), 1
    ),
    "disc_disc4_gcs_input4 ": AreaAnalyzeClass(
        uuid.UUID("CC5F60C2-8FDD-4AF3-A0ED-167822411F69"), 1
    ),
    "disc_disc4_gcs_input5 ": AreaAnalyzeClass(
        uuid.UUID("D9EC889B-B3C0-4867-9409-6E7E222EB2FE"), 1
    ),
    "disc_disc4_gcs_input6 ": AreaAnalyzeClass(
        uuid.UUID("B9CFC041-0BC3-4A03-B3F9-97EEA83B680A"), 1
    ),
    "disc_disc4_gcs_input7 ": AreaAnalyzeClass(
        uuid.UUID("02705493-FBD5-4079-A40C-14890120639B"), 1
    ),
    "disc_disc4_gcs_input8 ": AreaAnalyzeClass(
        uuid.UUID("B6F13DFA-1235-4CA1-8B1A-7AAE1F4FEE7B"), 1
    ),
    "disc_disc4_gcs_input9 ": AreaAnalyzeClass(
        uuid.UUID("30DAEE04-E70D-4027-A33A-BE20FF291B40"), 1
    ),
    "disc_disc4_gcs_std": AreaAnalyzeClass(
        uuid.UUID("75F6DD27-F6C4-401E-905B-6E2C57D27662"), 2
    ),
    "disc_disc4_moisture_input": AreaAnalyzeClass(
        uuid.UUID("75EF5B9D-0546-4414-9391-4B7F3E987880"), 1
    ),
    "disc_disc4_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("AC7C3C78-450E-4BDB-8617-DD528CDF51CB"), 1
    ),
    "disc_disc4_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("CF76DE51-8C60-492C-8084-826B0F6468B8"), 2
    ),
    "disc_disc4_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("1168F9B8-D000-47A6-8896-136F8D00AB13"), 1
    ),
    "disc_disc4_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("39798A8F-C51E-430A-9C19-1E519F71DEDB"), 2
    ),
    "disc_disc4_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("8DF7F480-940A-4DD9-B3C4-BB9DCF3F78AB"), 1
    ),
    "disc_disc4_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("547E995F-BD8B-4C6A-9366-96ADEB1CA31D"), 2
    ),
    "disc_disc4_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("3D705419-0990-4A9A-AFA2-4F29078449F4"), 1
    ),
    "disc_disc4_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("53B41EBB-AC2C-4F2A-868D-B98C5FF3290A"), 2
    ),
    "disc_disc4_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("F07E824B-AFF9-4169-894C-66286D841DD3"), 1
    ),
    "disc_disc4_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("819751FD-91BD-44F7-8E4F-7186C48AD5F1"), 2
    ),
    "disc_disc4_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("1BDDAF21-D112-4AC4-B149-AB722752790F"), 1
    ),
    "disc_disc5_drop_avg": AreaAnalyzeClass(
        uuid.UUID("9874452E-85B1-40D8-B618-F3470075E0C3"), 2
    ),
    "disc_disc5_drop_input1 ": AreaAnalyzeClass(
        uuid.UUID("534E3BF4-8362-43D8-AB09-33F9318E1E59"), 1
    ),
    "disc_disc5_drop_input10": AreaAnalyzeClass(
        uuid.UUID("850115DD-8FC3-4560-AF31-3B2B0B7B7B16"), 1
    ),
    "disc_disc5_drop_input11": AreaAnalyzeClass(
        uuid.UUID("FB01E185-AC3E-4E10-B704-0E42C55CA075"), 1
    ),
    "disc_disc5_drop_input12": AreaAnalyzeClass(
        uuid.UUID("DAB98B09-FD71-43D2-B374-25BE5E3708CE"), 1
    ),
    "disc_disc5_drop_input2 ": AreaAnalyzeClass(
        uuid.UUID("D92F9A9C-CDCA-4E97-B169-4FD227CB9A72"), 1
    ),
    "disc_disc5_drop_input3 ": AreaAnalyzeClass(
        uuid.UUID("3F67068A-0B22-4211-97B2-D63A55349F05"), 1
    ),
    "disc_disc5_drop_input4 ": AreaAnalyzeClass(
        uuid.UUID("68D5D03A-6919-4365-95CC-1778DD19E1AC"), 1
    ),
    "disc_disc5_drop_input5": AreaAnalyzeClass(
        uuid.UUID("875E8E1E-340C-4CC6-96A5-730770F32CDB"), 1
    ),
    "disc_disc5_drop_input6 ": AreaAnalyzeClass(
        uuid.UUID("F27B8D69-3B1B-4BE9-BE4E-AEDA70E789BA"), 1
    ),
    "disc_disc5_drop_input7 ": AreaAnalyzeClass(
        uuid.UUID("5A89F9E0-8E72-4428-B9B2-2EEC972A3846"), 1
    ),
    "disc_disc5_drop_input8 ": AreaAnalyzeClass(
        uuid.UUID("F6EB20BA-DA42-49B4-8BE6-37803FEF8CB7"), 1
    ),
    "disc_disc5_drop_input9 ": AreaAnalyzeClass(
        uuid.UUID("FF520C38-61D8-4DA2-87CE-531A7AA220A2"), 1
    ),
    "disc_disc5_drop_std": AreaAnalyzeClass(
        uuid.UUID("F5AB6D72-4E07-41BF-A9AC-89425E732478"), 2
    ),
    "disc_disc5_gcs_avg": AreaAnalyzeClass(
        uuid.UUID("0E531DE7-8DBE-4910-9FE9-E3764BD810D2"), 2
    ),
    "disc_disc5_gcs_input1 ": AreaAnalyzeClass(
        uuid.UUID("50502162-D6EF-4C9C-A06D-D6BEF0D18683"), 1
    ),
    "disc_disc5_gcs_input10": AreaAnalyzeClass(
        uuid.UUID("C1F3D735-782E-461D-8DB2-61232A352629"), 1
    ),
    "disc_disc5_gcs_input11": AreaAnalyzeClass(
        uuid.UUID("D0DEAB8A-3008-41E6-8B66-45E36516C67F"), 1
    ),
    "disc_disc5_gcs_input12": AreaAnalyzeClass(
        uuid.UUID("7792B861-590A-43B2-A93E-836DEDE46097"), 1
    ),
    "disc_disc5_gcs_input2 ": AreaAnalyzeClass(
        uuid.UUID("EEFC97A1-CA61-43B4-87ED-B93E2A310DA2"), 1
    ),
    "disc_disc5_gcs_input3 ": AreaAnalyzeClass(
        uuid.UUID("6415A6BF-0FFE-40B9-BDCE-CD88840B414A"), 1
    ),
    "disc_disc5_gcs_input4 ": AreaAnalyzeClass(
        uuid.UUID("D07D1ED0-CF6E-40B1-8FA7-5BFB239D7C59"), 1
    ),
    "disc_disc5_gcs_input5 ": AreaAnalyzeClass(
        uuid.UUID("D39A90C2-DAE7-487B-8FF9-879FCA0C9233"), 1
    ),
    "disc_disc5_gcs_input6 ": AreaAnalyzeClass(
        uuid.UUID("B976453A-7521-454D-B86F-BC713546B17F"), 1
    ),
    "disc_disc5_gcs_input7 ": AreaAnalyzeClass(
        uuid.UUID("36D61E36-7B25-4246-8623-FEFEBA950307"), 1
    ),
    "disc_disc5_gcs_input8 ": AreaAnalyzeClass(
        uuid.UUID("83BDA8C3-2CF9-4436-B7B2-E3BD86DF2A43"), 1
    ),
    "disc_disc5_gcs_input9 ": AreaAnalyzeClass(
        uuid.UUID("5DDCDE8D-4E9E-404C-B070-D31992398710"), 1
    ),
    "disc_disc5_gcs_std": AreaAnalyzeClass(
        uuid.UUID("77891F1B-443C-4363-8712-BC68D7938FA2"), 2
    ),
    "disc_disc5_moisture_input": AreaAnalyzeClass(
        uuid.UUID("2820F422-E7AC-4F19-B603-A54E58BCB03B"), 1
    ),
    "disc_disc5_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("6E626347-B210-4233-A899-2DE3362E8462"), 1
    ),
    "disc_disc5_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("56A344B1-2D53-4610-BB86-4F9077CBB572"), 2
    ),
    "disc_disc5_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("732648DB-029A-41DD-B45C-031CFAB0B472"), 1
    ),
    "disc_disc5_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("5EDD8CA3-9002-4F31-82A7-F35B8DBD1724"), 2
    ),
    "disc_disc5_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("8BAF0D2D-2083-44E5-90AC-11A0BB0B2B94"), 1
    ),
    "disc_disc5_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("459CB9A0-A08A-4B28-B6FC-98D5C4B809EB"), 2
    ),
    "disc_disc5_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("F45DE3A1-90E2-4D24-BDFD-92404B4DE724"), 1
    ),
    "disc_disc5_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("0572E906-993C-4EB9-87D2-5113B8999461"), 2
    ),
    "disc_disc5_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("FD85A1E5-4FA3-46B2-AB7C-BD2489354DE6"), 1
    ),
    "disc_disc5_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("095193E2-8856-47B5-A5DB-003F0F30A1B5"), 2
    ),
    "disc_disc5_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("E4669265-EE05-4716-A5BD-E6FED6563D01"), 1
    ),
    "disc_disc6_drop_avg": AreaAnalyzeClass(
        uuid.UUID("A67EBB81-2A9C-4DDA-8DE7-871DE354EC17"), 2
    ),
    "disc_disc6_drop_input1 ": AreaAnalyzeClass(
        uuid.UUID("9BF937BD-B334-4B56-BB1F-60A96ACBB48C"), 1
    ),
    "disc_disc6_drop_input10": AreaAnalyzeClass(
        uuid.UUID("982F310A-5195-4859-A220-7868EBBFC9CF"), 1
    ),
    "disc_disc6_drop_input11": AreaAnalyzeClass(
        uuid.UUID("4D1D0C33-1F72-490B-A073-3D84D6D05067"), 1
    ),
    "disc_disc6_drop_input12": AreaAnalyzeClass(
        uuid.UUID("5253F9CB-E42D-413E-B022-04759AD24B79"), 1
    ),
    "disc_disc6_drop_input2 ": AreaAnalyzeClass(
        uuid.UUID("39B5B731-09D3-49EC-9954-6E5FCD67B9DA"), 1
    ),
    "disc_disc6_drop_input3 ": AreaAnalyzeClass(
        uuid.UUID("B49A17E7-5583-41B3-9DAD-A585F18D45E0"), 1
    ),
    "disc_disc6_drop_input4 ": AreaAnalyzeClass(
        uuid.UUID("D3B77676-9995-40E1-81B1-EC2666E5AF1B"), 1
    ),
    "disc_disc6_drop_input5": AreaAnalyzeClass(
        uuid.UUID("A90D1621-4F57-4EF5-B5F6-49891CD8A8F8"), 1
    ),
    "disc_disc6_drop_input6 ": AreaAnalyzeClass(
        uuid.UUID("9E8C3303-AB38-44F5-AB41-216445AC0A8C"), 1
    ),
    "disc_disc6_drop_input7 ": AreaAnalyzeClass(
        uuid.UUID("65CF2D33-EA9E-427B-A268-48D5387EC429"), 1
    ),
    "disc_disc6_drop_input8 ": AreaAnalyzeClass(
        uuid.UUID("A575DBA4-BD98-4CE2-9E88-9F53C859F95A"), 1
    ),
    "disc_disc6_drop_input9 ": AreaAnalyzeClass(
        uuid.UUID("136C6432-479F-44C6-8C3C-5EB3618C5293"), 1
    ),
    "disc_disc6_drop_std": AreaAnalyzeClass(
        uuid.UUID("7711954D-983E-47AF-A138-8B1C16718868"), 2
    ),
    "disc_disc6_gcs_avg": AreaAnalyzeClass(
        uuid.UUID("2CCE0FD5-A1EA-4C31-ABB5-F34C758677CE"), 2
    ),
    "disc_disc6_gcs_input1 ": AreaAnalyzeClass(
        uuid.UUID("441E1DEE-B1B7-42CA-A6E1-5B87FA284E59"), 1
    ),
    "disc_disc6_gcs_input10": AreaAnalyzeClass(
        uuid.UUID("52A37877-8899-4BE9-AA90-1EABBE5C64AF"), 1
    ),
    "disc_disc6_gcs_input11": AreaAnalyzeClass(
        uuid.UUID("D944C29D-E92D-4437-A38A-D01A97C6E438"), 1
    ),
    "disc_disc6_gcs_input12": AreaAnalyzeClass(
        uuid.UUID("74F01DE4-CE25-4022-B2B8-55176F815A9D"), 1
    ),
    "disc_disc6_gcs_input2 ": AreaAnalyzeClass(
        uuid.UUID("911F119C-CFA4-4A52-9960-82D5B6FD424B"), 1
    ),
    "disc_disc6_gcs_input3 ": AreaAnalyzeClass(
        uuid.UUID("B9DCC0EF-A0A9-4067-A6E7-B1C8C15F1E71"), 1
    ),
    "disc_disc6_gcs_input4 ": AreaAnalyzeClass(
        uuid.UUID("EB6C820C-6A1E-412C-B83A-07A831912DD2"), 1
    ),
    "disc_disc6_gcs_input5 ": AreaAnalyzeClass(
        uuid.UUID("7CECA891-0BDC-42D5-B0C9-06A294F85197"), 1
    ),
    "disc_disc6_gcs_input6 ": AreaAnalyzeClass(
        uuid.UUID("A8D5CDE3-A37E-43BF-8AD4-3204FF373023"), 1
    ),
    "disc_disc6_gcs_input7 ": AreaAnalyzeClass(
        uuid.UUID("7AABB2F5-63A0-47C4-BBA3-9D8997768C82"), 1
    ),
    "disc_disc6_gcs_input8 ": AreaAnalyzeClass(
        uuid.UUID("525E894D-B763-4167-A48F-6EF1465FBEE8"), 1
    ),
    "disc_disc6_gcs_input9 ": AreaAnalyzeClass(
        uuid.UUID("1E823DC6-9294-4919-99B9-6FAB7AB26446"), 1
    ),
    "disc_disc6_gcs_std": AreaAnalyzeClass(
        uuid.UUID("756F975E-7FC9-4A33-88F7-DB5F14B53C2C"), 2
    ),
    "disc_disc6_moisture_input": AreaAnalyzeClass(
        uuid.UUID("496211CD-FFEE-4B64-A60E-7AD7D6D515E7"), 1
    ),
    "disc_disc6_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("A8096F46-7969-481C-B53E-80C7F6EE50FD"), 1
    ),
    "disc_disc6_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("C8BC3EB3-12F7-4F7F-96FF-FFC64562FE23"), 2
    ),
    "disc_disc6_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("A830AFF1-7679-41D3-BEA1-7E2DACF10694"), 1
    ),
    "disc_disc6_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("E47BFAFA-BE8A-46DA-B95E-B1B3DB81BAC4"), 2
    ),
    "disc_disc6_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("8AF03030-1CE8-4AF6-9CD7-F88DAC51B265"), 1
    ),
    "disc_disc6_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("C5701529-A67A-411A-9CA2-43B955C7AFAE"), 2
    ),
    "disc_disc6_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("E40A682A-81CD-494A-B91A-B4FD39BC4989"), 1
    ),
    "disc_disc6_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("2FE7DD1E-FB9B-4E55-86E4-077352FBB1F5"), 2
    ),
    "disc_disc6_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("EF1F4462-8DEA-4377-96A6-9FB46CC7BC77"), 1
    ),
    "disc_disc6_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("786B33E9-84A3-4871-B4F3-AC1A968E7D8A"), 2
    ),
    "disc_disc6_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("846CA253-11E6-40D9-B473-4D4268F9869F"), 1
    ),
    "limestone_limestone_cao_input": AreaAnalyzeClass(
        uuid.UUID("665ABE08-2AD5-4366-A8CF-3ABA512B19EA"), 2
    ),
    "limestone_limestone_loi_input": AreaAnalyzeClass(
        uuid.UUID("AB32E69B-EE5D-479E-9541-4507DC802AEB"), 2
    ),
    "limestone_limestone_mgo_input": AreaAnalyzeClass(
        uuid.UUID("678249DF-A677-4E6E-B836-611BEFC28026"), 2
    ),
    "limestone_limestone_moisture_input": AreaAnalyzeClass(
        uuid.UUID("221EA732-953E-477A-81DA-980C6F966A3E"), 1
    ),
    "limestone_limestone_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("F5BA3872-37DF-4682-9E14-5430B5711A40"), 1
    ),
    "limestone_limestone_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("7C615C30-7EB1-4622-8A20-65B1E8B489A5"), 2
    ),
    "limestone_limestone_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("4FFD2025-ECCC-4129-A236-8F0E2DB9D6D8"), 1
    ),
    "limestone_limestone_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("A979D539-7F4F-42C5-902A-C42335DA06DA"), 2
    ),
    "limestone_limestone_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("12918109-FCA6-4CDD-B1B8-CBD287E6861C"), 1
    ),
    "limestone_limestone_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("289E8A26-F7E9-4A00-850A-8D65D3623EC3"), 2
    ),
    "limestone_limestone_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("71C85D87-79A3-4B76-9E05-791554226884"), 1
    ),
    "limestone_limestone_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("3E38E072-09E8-4EA1-B736-54C43DB97735"), 2
    ),
    "limestone_limestone_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("D6B37F03-9ED7-463A-9CB8-E54DC2C03563"), 1
    ),
    "limestone_limestone_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("928DA845-176A-4465-827F-40B2A2CAC343"), 2
    ),
    "limestone_limestone_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("7B4C831B-9362-46B8-A619-5CE8B7361D9E"), 1
    ),
    "limestone_limestone_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("361C0128-4D13-4A3E-987D-91C608A4F440"), 1
    ),
    "limestone_limestone_xray_cao": AreaAnalyzeClass(
        uuid.UUID("395DC069-33DA-4AD8-B622-8D1C8608CB83"), 1
    ),
    "limestone_limestone_xray_fe": AreaAnalyzeClass(
        uuid.UUID("D928E472-92D7-46FB-8968-8B356FF8FA74"), 1
    ),
    "limestone_limestone_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("27234053-EF23-4818-AB09-4A21D01A3F18"), 1
    ),
    "limestone_limestone_xray_mno": AreaAnalyzeClass(
        uuid.UUID("1E2F0BA3-F1FE-4365-BDD5-A80B2F9E09C2"), 1
    ),
    "limestone_limestone_xray_p": AreaAnalyzeClass(
        uuid.UUID("4680E45A-5B45-404A-8245-D3D95D2CD0D1"), 1
    ),
    "limestone_limestone_xray_result": AreaAnalyzeClass(
        uuid.UUID("8ED7A29A-B963-4951-8B6B-EC2909306E84"), 2
    ),
    "limestone_limestone_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("AF02C11B-FA99-4678-93EA-95865D5FED9A"), 1
    ),
    "limestone_limestone_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("8E5B1BCF-83B4-46BE-A785-E2B4A4DC98DB"), 1
    ),
    "pelletchip_pelletchip_feo_avg": AreaAnalyzeClass(
        uuid.UUID("E5E07CCD-2AC5-4B76-A309-D5585255B611"), 2
    ),
    "pelletchip_pelletchip_feo_input1": AreaAnalyzeClass(
        uuid.UUID("FCF169B4-C3DC-444C-A829-9382C6A2AB11"), 1
    ),
    "pelletchip_pelletchip_feo_input2": AreaAnalyzeClass(
        uuid.UUID("86164391-A123-4C98-B31E-AEB1A32A3511"), 1
    ),
    "pelletchip_pelletchip_moisture_input": AreaAnalyzeClass(
        uuid.UUID("06711C68-AA51-44DF-BB12-7362E45CBB11"), 1
    ),
    "pelletchip_pelletchip_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("B46E7014-7F33-4CD7-8B54-F7425F265A11"), 1
    ),
    "pelletchip_pelletchip_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("45921446-1029-4328-92DA-2A160D1E0111"), 2
    ),
    "pelletchip_pelletchip_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("62B434D0-4A93-483C-92BD-211ECAC4EF11"), 1
    ),
    "pelletchip_pelletchip_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("699BBEA1-D871-4613-98D5-D633AD8AED11"), 2
    ),
    "pelletchip_pelletchip_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("6BF3D329-4DF2-404E-A915-E068FF7DCE11"), 1
    ),
    "pelletchip_pelletchip_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("DD9231C2-EDE6-4CD6-94F3-5E429659B211"), 2
    ),
    "pelletchip_pelletchip_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("925A82F4-31B3-4304-AC5D-3545F021EA11"), 1
    ),
    "pelletchip_pelletchip_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("BDA6D73D-BD62-4634-AF86-EC6092614311"), 2
    ),
    "pelletchip_pelletchip_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("8714DDA8-AD5B-482A-903C-F0CB953CF111"), 1
    ),
    "pelletchip_pelletchip_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("CB98E6B4-CB5B-484C-86B3-0E2EE61D8B11"), 2
    ),
    "pelletchip_pelletchip_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("4431FC5C-0913-44B8-8326-150B26C44011"), 1
    ),
    "pelletchip_pelletchip_sulfur_input": AreaAnalyzeClass(
        uuid.UUID("A536D56E-C42D-4227-846E-32568A2B2511"), 1
    ),
    "pelletchip_pelletchip_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("35031E4D-B5BE-4BC8-A248-A01120E81911"), 2
    ),
    "pelletchip_pelletchip_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("C29A63E7-CE00-46AA-AA13-1329F67EE311"), 1
    ),
    "pelletchip_pelletchip_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("A0304167-4F3B-428D-A9AA-206E233BFF11"), 1
    ),
    "pelletchip_pelletchip_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("60326116-5BCF-456A-9049-55A206DAB711"), 1
    ),
    "pelletchip_pelletchip_xray_cao": AreaAnalyzeClass(
        uuid.UUID("FB2746DB-9163-4AFC-A2C9-980ECCF44911"), 1
    ),
    "pelletchip_pelletchip_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("1A8A9E63-E5B3-4737-B2F3-4634CD94F611"), 1
    ),
    "pelletchip_pelletchip_xray_mno": AreaAnalyzeClass(
        uuid.UUID("7472D652-C292-4924-AA46-8A29D03A1911"), 1
    ),
    "pelletchip_pelletchip_xray_p": AreaAnalyzeClass(
        uuid.UUID("80CF2672-DB43-45BB-BD53-83AF24DA0411"), 1
    ),
    "pelletchip_pelletchip_xray_result": AreaAnalyzeClass(
        uuid.UUID("B4D407D1-5858-4DCE-A751-AAACCAF6EF11"), 2
    ),
    "pelletchip_pelletchip_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("DE9FB1A5-04C8-4290-AE58-7EFAB0145811"), 1
    ),
    "pelletchip_pelletchip_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("6EA30BD5-D55C-4636-9CAC-59EC5B2BDD11"), 1
    ),
    "reducedtest_linderreduction_ccs_100": AreaAnalyzeClass(
        uuid.UUID("3212FA1C-8E74-46C9-AA7B-C5D1182D8DE8"), 2
    ),
    "reducedtest_linderreduction_ccs_150": AreaAnalyzeClass(
        uuid.UUID("B7B6F1FF-F141-4C1F-AD63-0DB5AA4D7C54"), 2
    ),
    "reducedtest_linderreduction_ccs_50": AreaAnalyzeClass(
        uuid.UUID("B87979CD-5FE7-440B-B741-BD4EA52FBC79"), 2
    ),
    "reducedtest_linderreduction_ccs_avg": AreaAnalyzeClass(
        uuid.UUID("842BF1DE-50A5-4182-A178-2CE394B5B065"), 2
    ),
    "reducedtest_linderreduction_ccs_input1": AreaAnalyzeClass(
        uuid.UUID("F3E9259C-E36F-470B-B798-668CAFEB6DB2"), 1
    ),
    "reducedtest_linderreduction_ccs_input10": AreaAnalyzeClass(
        uuid.UUID("0F4B8354-C812-4075-8C43-F61C88017A55"), 1
    ),
    "reducedtest_linderreduction_ccs_input100": AreaAnalyzeClass(
        uuid.UUID("85F58B32-8A13-4B3A-94B2-70D265E50054"), 1
    ),
    "reducedtest_linderreduction_ccs_input11": AreaAnalyzeClass(
        uuid.UUID("0B4B46BE-FA33-4D3C-BF11-1101F4C46DAD"), 1
    ),
    "reducedtest_linderreduction_ccs_input12": AreaAnalyzeClass(
        uuid.UUID("791044F6-D0A6-484C-9D81-59839D621D44"), 1
    ),
    "reducedtest_linderreduction_ccs_input13": AreaAnalyzeClass(
        uuid.UUID("3479DFA0-2463-4210-9C80-74B9402D7D79"), 1
    ),
    "reducedtest_linderreduction_ccs_input14": AreaAnalyzeClass(
        uuid.UUID("663F2736-64B1-444F-82B8-1D393FB4513C"), 1
    ),
    "reducedtest_linderreduction_ccs_input15": AreaAnalyzeClass(
        uuid.UUID("70DCDFFC-CE4C-4C52-988D-94C0CD6DC4BC"), 1
    ),
    "reducedtest_linderreduction_ccs_input16": AreaAnalyzeClass(
        uuid.UUID("A8724E42-FCE2-4804-AB9A-51D4EE976C6C"), 1
    ),
    "reducedtest_linderreduction_ccs_input17": AreaAnalyzeClass(
        uuid.UUID("A7400CE0-FE5B-4E95-AD5F-916E33CAF5A2"), 1
    ),
    "reducedtest_linderreduction_ccs_input18": AreaAnalyzeClass(
        uuid.UUID("5F031A40-C6D8-435F-98BC-A2F866EF7720"), 1
    ),
    "reducedtest_linderreduction_ccs_input19": AreaAnalyzeClass(
        uuid.UUID("F403A473-818E-4130-81BF-8FFB7F9DACBB"), 1
    ),
    "reducedtest_linderreduction_ccs_input2": AreaAnalyzeClass(
        uuid.UUID("594E5ACC-455C-4349-B25B-29BF1FBB008A"), 1
    ),
    "reducedtest_linderreduction_ccs_input20": AreaAnalyzeClass(
        uuid.UUID("4CA85EC3-5530-48ED-A2FB-30B31690011A"), 1
    ),
    "reducedtest_linderreduction_ccs_input21": AreaAnalyzeClass(
        uuid.UUID("CA993D69-3489-49FB-9507-F1F9EA0001CD"), 1
    ),
    "reducedtest_linderreduction_ccs_input22": AreaAnalyzeClass(
        uuid.UUID("7C49A68A-A4C2-4C3E-A485-7936609C4830"), 1
    ),
    "reducedtest_linderreduction_ccs_input23": AreaAnalyzeClass(
        uuid.UUID("A5E1F585-54FA-478D-86D6-173A95EFA7B1"), 1
    ),
    "reducedtest_linderreduction_ccs_input24": AreaAnalyzeClass(
        uuid.UUID("8EC4BABE-2F41-4FF1-8820-83C296BF0518"), 1
    ),
    "reducedtest_linderreduction_ccs_input25": AreaAnalyzeClass(
        uuid.UUID("E46EA2B1-1344-47D2-BEF1-BF71E56EB380"), 1
    ),
    "reducedtest_linderreduction_ccs_input26": AreaAnalyzeClass(
        uuid.UUID("89E52F7D-D53A-4E6E-A46C-EACAD93A5AB6"), 1
    ),
    "reducedtest_linderreduction_ccs_input27": AreaAnalyzeClass(
        uuid.UUID("2C70CADA-776F-4DDE-884A-CFDCF77A349D"), 1
    ),
    "reducedtest_linderreduction_ccs_input28": AreaAnalyzeClass(
        uuid.UUID("60C612F5-C115-4B7B-8A18-D5B4600EF2BF"), 1
    ),
    "reducedtest_linderreduction_ccs_input29": AreaAnalyzeClass(
        uuid.UUID("E8F6C542-C897-41E1-BF09-7B6E1BA8619F"), 1
    ),
    "reducedtest_linderreduction_ccs_input3": AreaAnalyzeClass(
        uuid.UUID("075C5EF5-0FEE-4267-A293-7245C4396B40"), 1
    ),
    "reducedtest_linderreduction_ccs_input30": AreaAnalyzeClass(
        uuid.UUID("E3737ECD-37AB-44A4-B55A-5113AD9CA9AF"), 1
    ),
    "reducedtest_linderreduction_ccs_input31": AreaAnalyzeClass(
        uuid.UUID("6E6E619E-4DB1-4D2A-AAD4-C47D5D97D987"), 1
    ),
    "reducedtest_linderreduction_ccs_input32": AreaAnalyzeClass(
        uuid.UUID("00CFE1A5-D6D4-4B09-A7E4-40B5FB2687D4"), 1
    ),
    "reducedtest_linderreduction_ccs_input33": AreaAnalyzeClass(
        uuid.UUID("5F64B542-F686-40D2-A5D6-8F74AE8D290C"), 1
    ),
    "reducedtest_linderreduction_ccs_input34": AreaAnalyzeClass(
        uuid.UUID("8ACE8A8B-AD0F-4F36-AE07-1B7274209B93"), 1
    ),
    "reducedtest_linderreduction_ccs_input35": AreaAnalyzeClass(
        uuid.UUID("56976139-F9C9-4A35-9145-8AC81AF14152"), 1
    ),
    "reducedtest_linderreduction_ccs_input36": AreaAnalyzeClass(
        uuid.UUID("959097E5-ECA0-444F-BB13-308C7F654585"), 1
    ),
    "reducedtest_linderreduction_ccs_input37": AreaAnalyzeClass(
        uuid.UUID("1A6FDAB4-9917-4CD8-958E-8B0AE79724F2"), 1
    ),
    "reducedtest_linderreduction_ccs_input38": AreaAnalyzeClass(
        uuid.UUID("9B74020F-C5BD-4E5C-B456-80E7C222E4BD"), 1
    ),
    "reducedtest_linderreduction_ccs_input39": AreaAnalyzeClass(
        uuid.UUID("46841CAD-9D32-4B1F-B71A-422C2F7FAC19"), 1
    ),
    "reducedtest_linderreduction_ccs_input4": AreaAnalyzeClass(
        uuid.UUID("08043E03-C549-4066-A2BC-07F63C5CBFE1"), 1
    ),
    "reducedtest_linderreduction_ccs_input40": AreaAnalyzeClass(
        uuid.UUID("ADF1D7E1-EC6A-482C-B0D3-D21631549115"), 1
    ),
    "reducedtest_linderreduction_ccs_input41": AreaAnalyzeClass(
        uuid.UUID("6EF7318B-B36E-4150-9DAD-1086957D497E"), 1
    ),
    "reducedtest_linderreduction_ccs_input42": AreaAnalyzeClass(
        uuid.UUID("1080C47F-EA5C-4816-B26C-A5F4B82892B1"), 1
    ),
    "reducedtest_linderreduction_ccs_input43": AreaAnalyzeClass(
        uuid.UUID("AA2AF40A-EBD9-43E8-8D28-B3D05AA34AA6"), 1
    ),
    "reducedtest_linderreduction_ccs_input44": AreaAnalyzeClass(
        uuid.UUID("79717C99-1E59-47A5-9D4F-E16609A60FAF"), 1
    ),
    "reducedtest_linderreduction_ccs_input45": AreaAnalyzeClass(
        uuid.UUID("5F3EEFFC-CE36-4982-BFE6-0D6807E4685D"), 1
    ),
    "reducedtest_linderreduction_ccs_input46": AreaAnalyzeClass(
        uuid.UUID("BE60D5C9-D138-46DF-855B-E0A8D01CD947"), 1
    ),
    "reducedtest_linderreduction_ccs_input47": AreaAnalyzeClass(
        uuid.UUID("A651E97C-DAF2-41B2-8594-062C3729B9F9"), 1
    ),
    "reducedtest_linderreduction_ccs_input48": AreaAnalyzeClass(
        uuid.UUID("E9EDC7D7-F35C-4D6B-B1B4-C99542136826"), 1
    ),
    "reducedtest_linderreduction_ccs_input49": AreaAnalyzeClass(
        uuid.UUID("E2ACBA89-339F-42BE-9FD9-E3E78390453C"), 1
    ),
    "reducedtest_linderreduction_ccs_input5": AreaAnalyzeClass(
        uuid.UUID("9787032C-3DAB-4C51-A970-0FA287C641AF"), 1
    ),
    "reducedtest_linderreduction_ccs_input50": AreaAnalyzeClass(
        uuid.UUID("47304A05-C76A-4AE9-AD30-6C0BDCE07E41"), 1
    ),
    "reducedtest_linderreduction_ccs_input51": AreaAnalyzeClass(
        uuid.UUID("567B2DA4-7DF4-43BD-B6D2-7644CFC25BD7"), 1
    ),
    "reducedtest_linderreduction_ccs_input52": AreaAnalyzeClass(
        uuid.UUID("5F79276D-5BC4-4DCD-9AA6-DBFB53BA6F7C"), 1
    ),
    "reducedtest_linderreduction_ccs_input53": AreaAnalyzeClass(
        uuid.UUID("DC082E13-1724-40AE-8DA2-A4E06F247B17"), 1
    ),
    "reducedtest_linderreduction_ccs_input54": AreaAnalyzeClass(
        uuid.UUID("D3461FF0-777B-4235-92DF-F09A9CEE9637"), 1
    ),
    "reducedtest_linderreduction_ccs_input55": AreaAnalyzeClass(
        uuid.UUID("0259E095-ECD9-469D-B7FE-56609B028E02"), 1
    ),
    "reducedtest_linderreduction_ccs_input56": AreaAnalyzeClass(
        uuid.UUID("03D607AA-97DA-42D6-B2D0-3E3318AF02BD"), 1
    ),
    "reducedtest_linderreduction_ccs_input57": AreaAnalyzeClass(
        uuid.UUID("BD79B368-05C3-4A82-9EF1-8A2F265166B1"), 1
    ),
    "reducedtest_linderreduction_ccs_input58": AreaAnalyzeClass(
        uuid.UUID("4989035F-5BF3-4001-9322-E37E0928748C"), 1
    ),
    "reducedtest_linderreduction_ccs_input59": AreaAnalyzeClass(
        uuid.UUID("4CF2465D-40FC-447F-8D0B-3DF3F9862A0B"), 1
    ),
    "reducedtest_linderreduction_ccs_input6": AreaAnalyzeClass(
        uuid.UUID("BDAFF52D-3475-40BE-B039-A6EF3281FD36"), 1
    ),
    "reducedtest_linderreduction_ccs_input60": AreaAnalyzeClass(
        uuid.UUID("D55B8F1A-E0B8-4630-A2A7-DD189E99362A"), 1
    ),
    "reducedtest_linderreduction_ccs_input61": AreaAnalyzeClass(
        uuid.UUID("A5466ED8-58DD-4087-92B3-71ADB1DEF75A"), 1
    ),
    "reducedtest_linderreduction_ccs_input62": AreaAnalyzeClass(
        uuid.UUID("1DCDB2FD-DA23-41A3-9561-BC37C706268B"), 1
    ),
    "reducedtest_linderreduction_ccs_input63": AreaAnalyzeClass(
        uuid.UUID("1DC619C4-792F-4C31-9D67-88CB687FABDD"), 1
    ),
    "reducedtest_linderreduction_ccs_input64": AreaAnalyzeClass(
        uuid.UUID("7E4019AE-984D-454A-906A-18C9CD9F7A42"), 1
    ),
    "reducedtest_linderreduction_ccs_input65": AreaAnalyzeClass(
        uuid.UUID("40F54D6A-9358-48FA-AC36-F67D3836039C"), 1
    ),
    "reducedtest_linderreduction_ccs_input66": AreaAnalyzeClass(
        uuid.UUID("EB53BA72-7CC9-4995-8B13-A2788693614C"), 1
    ),
    "reducedtest_linderreduction_ccs_input67": AreaAnalyzeClass(
        uuid.UUID("5C089F47-409F-4E9B-9BD6-2DB9FD347C63"), 1
    ),
    "reducedtest_linderreduction_ccs_input68": AreaAnalyzeClass(
        uuid.UUID("B1FBA2C3-6A68-43A0-8CD0-83E17F6851DE"), 1
    ),
    "reducedtest_linderreduction_ccs_input69": AreaAnalyzeClass(
        uuid.UUID("ED7E901E-BA66-4525-9571-A370E34C9659"), 1
    ),
    "reducedtest_linderreduction_ccs_input7": AreaAnalyzeClass(
        uuid.UUID("FF4F9EE3-CCB9-4A33-BA5A-E2E445715E6C"), 1
    ),
    "reducedtest_linderreduction_ccs_input70": AreaAnalyzeClass(
        uuid.UUID("67A6004A-4F70-45B1-96EC-4ABB3FA5469B"), 1
    ),
    "reducedtest_linderreduction_ccs_input71": AreaAnalyzeClass(
        uuid.UUID("E0DCE2C1-6888-4040-9B7B-E8EE136D24B2"), 1
    ),
    "reducedtest_linderreduction_ccs_input72": AreaAnalyzeClass(
        uuid.UUID("920C60F8-21AB-4E59-BA5E-D1A188E21F5A"), 1
    ),
    "reducedtest_linderreduction_ccs_input73": AreaAnalyzeClass(
        uuid.UUID("77580438-EDD7-4E2A-8715-089CC9DE6D89"), 1
    ),
    "reducedtest_linderreduction_ccs_input74": AreaAnalyzeClass(
        uuid.UUID("9460D5AE-B050-4444-AFED-202D62804CD8"), 1
    ),
    "reducedtest_linderreduction_ccs_input75": AreaAnalyzeClass(
        uuid.UUID("6ADA2D38-520C-4CDD-AD0F-0B4F3CD87528"), 1
    ),
    "reducedtest_linderreduction_ccs_input76": AreaAnalyzeClass(
        uuid.UUID("B3651582-E460-4A68-B163-5CD1433F1DF0"), 1
    ),
    "reducedtest_linderreduction_ccs_input77": AreaAnalyzeClass(
        uuid.UUID("294F47D8-DD1F-434E-9573-E904FA424BD0"), 1
    ),
    "reducedtest_linderreduction_ccs_input78": AreaAnalyzeClass(
        uuid.UUID("B85B2AFB-F575-40A0-AA5B-B9669601885B"), 1
    ),
    "reducedtest_linderreduction_ccs_input79": AreaAnalyzeClass(
        uuid.UUID("4AB5A93F-3C50-496E-B3A9-5499BB209AAF"), 1
    ),
    "reducedtest_linderreduction_ccs_input8": AreaAnalyzeClass(
        uuid.UUID("EC036522-0D82-4596-8BDE-BC06BAD64277"), 1
    ),
    "reducedtest_linderreduction_ccs_input80": AreaAnalyzeClass(
        uuid.UUID("D3209A1A-046C-4DC3-8767-6BD2F54491B4"), 1
    ),
    "reducedtest_linderreduction_ccs_input81": AreaAnalyzeClass(
        uuid.UUID("207E543B-4A38-40E9-B76E-D2BB6C15E83B"), 1
    ),
    "reducedtest_linderreduction_ccs_input82": AreaAnalyzeClass(
        uuid.UUID("810647FB-E10F-454A-8A29-9C39E8C2E877"), 1
    ),
    "reducedtest_linderreduction_ccs_input83": AreaAnalyzeClass(
        uuid.UUID("847CBADF-69A7-47BC-A2BF-0CB3025A4139"), 1
    ),
    "reducedtest_linderreduction_ccs_input84": AreaAnalyzeClass(
        uuid.UUID("E2161886-154B-41CA-B96B-69DD3AAE27C4"), 1
    ),
    "reducedtest_linderreduction_ccs_input85": AreaAnalyzeClass(
        uuid.UUID("F65A8145-8FDE-4A76-80E3-5C8CB33CF13D"), 1
    ),
    "reducedtest_linderreduction_ccs_input86": AreaAnalyzeClass(
        uuid.UUID("5A515F69-FC3B-4C4F-9311-07F93572D12A"), 1
    ),
    "reducedtest_linderreduction_ccs_input87": AreaAnalyzeClass(
        uuid.UUID("52EE669A-64A8-428B-8714-EBF2F79F4E8C"), 1
    ),
    "reducedtest_linderreduction_ccs_input88": AreaAnalyzeClass(
        uuid.UUID("B3C96A81-E90E-450E-9A38-6D53B042C570"), 1
    ),
    "reducedtest_linderreduction_ccs_input89": AreaAnalyzeClass(
        uuid.UUID("83CA5884-122E-4F54-A4E6-D0C9ABF1D060"), 1
    ),
    "reducedtest_linderreduction_ccs_input9": AreaAnalyzeClass(
        uuid.UUID("7BBA05FF-7964-411E-933F-9458D6623647"), 1
    ),
    "reducedtest_linderreduction_ccs_input90": AreaAnalyzeClass(
        uuid.UUID("89806EA4-107E-455C-A197-2EEEE992FE5F"), 1
    ),
    "reducedtest_linderreduction_ccs_input91": AreaAnalyzeClass(
        uuid.UUID("0B77393B-F327-49D3-9FB2-17B5FC46B058"), 1
    ),
    "reducedtest_linderreduction_ccs_input92": AreaAnalyzeClass(
        uuid.UUID("4D62A042-F9D2-4B78-A565-3E9E5A1BAEB1"), 1
    ),
    "reducedtest_linderreduction_ccs_input93": AreaAnalyzeClass(
        uuid.UUID("C878FFBB-9DAA-4E8D-908B-2B30AE86DA43"), 1
    ),
    "reducedtest_linderreduction_ccs_input94": AreaAnalyzeClass(
        uuid.UUID("1B7556EF-35F2-470F-93AD-DE7D8CE719BF"), 1
    ),
    "reducedtest_linderreduction_ccs_input95": AreaAnalyzeClass(
        uuid.UUID("6F9F9243-F247-45F7-8A18-4BECF90A9016"), 1
    ),
    "reducedtest_linderreduction_ccs_input96": AreaAnalyzeClass(
        uuid.UUID("B09DBBC6-7693-4C70-BAAB-1086FAD37B3C"), 1
    ),
    "reducedtest_linderreduction_ccs_input97": AreaAnalyzeClass(
        uuid.UUID("4A1543BA-946E-4D7A-A9EC-AFD22B557689"), 1
    ),
    "reducedtest_linderreduction_ccs_input98": AreaAnalyzeClass(
        uuid.UUID("5374F984-921A-4CCE-807C-7A7E41D3788E"), 1
    ),
    "reducedtest_linderreduction_ccs_input99": AreaAnalyzeClass(
        uuid.UUID("6D954790-1E70-450C-B7D3-04BF6D3C4D67"), 1
    ),
    "reducedtest_linderreduction_ccs_std": AreaAnalyzeClass(
        uuid.UUID("93790E75-EB34-412C-8507-D1677E19C700"), 2
    ),
    "reducedtest_linderreduction_fragmention_33563mm": AreaAnalyzeClass(
        uuid.UUID("7726324B-7922-4107-9F17-DC972B13BB50"), 1
    ),
    "reducedtest_linderreduction_fragmention_33563w": AreaAnalyzeClass(
        uuid.UUID("410E4DCF-8ED2-46B1-B853-CE25659CC029"), 1
    ),
    "reducedtest_linderreduction_fragmention_335mm": AreaAnalyzeClass(
        uuid.UUID("3D12F979-0EA5-4DCC-BCBF-FE6973644F2F"), 1
    ),
    "reducedtest_linderreduction_fragmention_335w": AreaAnalyzeClass(
        uuid.UUID("20CC8BB2-28F0-4812-BF22-B31CE7377EB3"), 1
    ),
    "reducedtest_linderreduction_fragmention_63mm": AreaAnalyzeClass(
        uuid.UUID("EA1AEEA0-6463-4093-AA44-DB5538C28085"), 1
    ),
    "reducedtest_linderreduction_fragmention_63w": AreaAnalyzeClass(
        uuid.UUID("973E2BFD-CB59-47F1-BC0C-E5C6797FCA15"), 1
    ),
    "reducedtest_linderreduction_fragmention_weight": AreaAnalyzeClass(
        uuid.UUID("BDE7F442-4B5C-4674-8F1B-0EA32152A7BF"), 1
    ),
    "reducedtest_linderreduction_mfe_input1": AreaAnalyzeClass(
        uuid.UUID("7C4E6A42-ABC0-464A-8BDE-1A667910D407"), 1
    ),
    "reducedtest_linderreduction_reducibility_feo": AreaAnalyzeClass(
        uuid.UUID("856AF45B-0669-46A4-A438-74744E1F7E56"), 1
    ),
    "reducedtest_linderreduction_reducibility_result": AreaAnalyzeClass(
        uuid.UUID("28B182CD-5B87-45FA-B98D-117D5E75E5BE"), 2
    ),
    "reducedtest_linderreduction_reducibility_tfe": AreaAnalyzeClass(
        uuid.UUID("6602287F-1641-4AB7-85FB-043EA1E4A7F2"), 1
    ),
    "reducedtest_linderreduction_reducibility_wafter": AreaAnalyzeClass(
        uuid.UUID("887F8BD8-DB3C-4FF2-8D00-B83622F1B2A2"), 1
    ),
    "reducedtest_linderreduction_reducibility_wbefore": AreaAnalyzeClass(
        uuid.UUID("163F21EA-83BC-4015-8A20-A8502BEBCDB8"), 1
    ),
    "reducedtest_linderreduction_tfeafter_input": AreaAnalyzeClass(
        uuid.UUID("7B6F3756-A9D7-49A2-9C1D-8A7BA8BACF7C"), 1
    ),
    "reducedtest_underloadreduction_ccs_100": AreaAnalyzeClass(
        uuid.UUID("A2C0D550-8F55-4766-9BFB-FF73795384F0"), 2
    ),
    "reducedtest_underloadreduction_ccs_150": AreaAnalyzeClass(
        uuid.UUID("D2E183DA-445C-4698-B328-A11ED0905930"), 2
    ),
    "reducedtest_underloadreduction_ccs_50": AreaAnalyzeClass(
        uuid.UUID("30C6E108-368E-4D65-AFDB-756E507A22D0"), 2
    ),
    "reducedtest_underloadreduction_ccs_avg": AreaAnalyzeClass(
        uuid.UUID("7862AE02-E7B2-4DFD-9B21-1ED835DF5BAB"), 2
    ),
    "reducedtest_underloadreduction_ccs_input1": AreaAnalyzeClass(
        uuid.UUID("7F66C964-9765-4D4F-AD82-77578D772E1E"), 1
    ),
    "reducedtest_underloadreduction_ccs_input10": AreaAnalyzeClass(
        uuid.UUID("091C7776-C721-435E-9E79-BB211A1484EC"), 1
    ),
    "reducedtest_underloadreduction_ccs_input100": AreaAnalyzeClass(
        uuid.UUID("8E7F2050-6C80-466E-B237-449B3D9AA09B"), 1
    ),
    "reducedtest_underloadreduction_ccs_input11": AreaAnalyzeClass(
        uuid.UUID("9FE076A8-05D9-48FF-83AB-41CECD21FC5E"), 1
    ),
    "reducedtest_underloadreduction_ccs_input12": AreaAnalyzeClass(
        uuid.UUID("F92C5171-6B64-4AAC-9601-CB1B4809D7C8"), 1
    ),
    "reducedtest_underloadreduction_ccs_input13": AreaAnalyzeClass(
        uuid.UUID("DACF7D3F-37EA-42E2-A790-CBC920AEB7D4"), 1
    ),
    "reducedtest_underloadreduction_ccs_input14": AreaAnalyzeClass(
        uuid.UUID("ACF1BEE9-7722-4814-AE72-DDF51DF431A1"), 1
    ),
    "reducedtest_underloadreduction_ccs_input15": AreaAnalyzeClass(
        uuid.UUID("FD519A28-5BFF-4C7C-9AC3-FFCE01A82BBB"), 1
    ),
    "reducedtest_underloadreduction_ccs_input16": AreaAnalyzeClass(
        uuid.UUID("7D12C9C6-DBB1-42D5-8168-A0E004C326DC"), 1
    ),
    "reducedtest_underloadreduction_ccs_input17": AreaAnalyzeClass(
        uuid.UUID("F1840313-912A-4F63-A5C9-5B6BCFD822E5"), 1
    ),
    "reducedtest_underloadreduction_ccs_input18": AreaAnalyzeClass(
        uuid.UUID("DAC3191D-D128-4A4F-AB63-2F3F15A51F7A"), 1
    ),
    "reducedtest_underloadreduction_ccs_input19": AreaAnalyzeClass(
        uuid.UUID("A62D2389-1099-472D-8081-D0BA159DC6F0"), 1
    ),
    "reducedtest_underloadreduction_ccs_input2": AreaAnalyzeClass(
        uuid.UUID("03AB995F-9B1F-4173-BA5E-6DF0BCD00522"), 1
    ),
    "reducedtest_underloadreduction_ccs_input20": AreaAnalyzeClass(
        uuid.UUID("8FB45B9C-4BDF-4A17-B10B-156483F7FEB2"), 1
    ),
    "reducedtest_underloadreduction_ccs_input21": AreaAnalyzeClass(
        uuid.UUID("22507BB8-8E88-492D-B523-A7B7C71A2451"), 1
    ),
    "reducedtest_underloadreduction_ccs_input22": AreaAnalyzeClass(
        uuid.UUID("0E0295E2-6508-4545-B482-86B50E737DDF"), 1
    ),
    "reducedtest_underloadreduction_ccs_input23": AreaAnalyzeClass(
        uuid.UUID("366A5951-7F25-48D8-9D78-8DF09769CC6B"), 1
    ),
    "reducedtest_underloadreduction_ccs_input24": AreaAnalyzeClass(
        uuid.UUID("B5D0329A-207F-4EBB-BD26-0CF79A7FEAD3"), 1
    ),
    "reducedtest_underloadreduction_ccs_input25": AreaAnalyzeClass(
        uuid.UUID("DD15B59C-E008-4A14-9314-3DDA798B684A"), 1
    ),
    "reducedtest_underloadreduction_ccs_input26": AreaAnalyzeClass(
        uuid.UUID("51A0799F-B1A3-4031-A67C-726258C8DE95"), 1
    ),
    "reducedtest_underloadreduction_ccs_input27": AreaAnalyzeClass(
        uuid.UUID("111CF588-E3C6-4F75-92A9-0D8DAA6C1DBF"), 1
    ),
    "reducedtest_underloadreduction_ccs_input28": AreaAnalyzeClass(
        uuid.UUID("F80F51EF-7D74-4250-9164-F61CE4F4D741"), 1
    ),
    "reducedtest_underloadreduction_ccs_input29": AreaAnalyzeClass(
        uuid.UUID("D0EB1943-A0B5-45AC-9790-1CA7A502F463"), 1
    ),
    "reducedtest_underloadreduction_ccs_input3": AreaAnalyzeClass(
        uuid.UUID("17496EE3-5CED-4B8E-A3B7-2EAEA15A7E3C"), 1
    ),
    "reducedtest_underloadreduction_ccs_input30": AreaAnalyzeClass(
        uuid.UUID("664E9DE4-C7AC-4405-A31D-CA1DD98453BE"), 1
    ),
    "reducedtest_underloadreduction_ccs_input31": AreaAnalyzeClass(
        uuid.UUID("2441BD36-439E-49C6-A8E5-42B8AB8937D5"), 1
    ),
    "reducedtest_underloadreduction_ccs_input32": AreaAnalyzeClass(
        uuid.UUID("A840E5F7-1E76-4494-95EC-27A37DEFB3C1"), 1
    ),
    "reducedtest_underloadreduction_ccs_input33": AreaAnalyzeClass(
        uuid.UUID("EDECFC04-A6D9-47F7-92F1-F3319AC680BE"), 1
    ),
    "reducedtest_underloadreduction_ccs_input34": AreaAnalyzeClass(
        uuid.UUID("CE92EBD5-4F4A-44E2-91E7-327488F67FDB"), 1
    ),
    "reducedtest_underloadreduction_ccs_input35": AreaAnalyzeClass(
        uuid.UUID("0B1C712E-242F-4EED-9B7D-2DE89FEABF1C"), 1
    ),
    "reducedtest_underloadreduction_ccs_input36": AreaAnalyzeClass(
        uuid.UUID("31830BA9-46F5-4B5C-BFD2-E3C379EBA6E8"), 1
    ),
    "reducedtest_underloadreduction_ccs_input37": AreaAnalyzeClass(
        uuid.UUID("7E1689BB-37F8-45EC-9D08-71978FEB973F"), 1
    ),
    "reducedtest_underloadreduction_ccs_input38": AreaAnalyzeClass(
        uuid.UUID("43AC68EF-1D9D-4B03-9D12-C4C22D1A41FF"), 1
    ),
    "reducedtest_underloadreduction_ccs_input39": AreaAnalyzeClass(
        uuid.UUID("077394E8-3E26-471F-AE18-4360B84FA126"), 1
    ),
    "reducedtest_underloadreduction_ccs_input4": AreaAnalyzeClass(
        uuid.UUID("11463654-78C4-4A06-987C-278EEC7C88DB"), 1
    ),
    "reducedtest_underloadreduction_ccs_input40": AreaAnalyzeClass(
        uuid.UUID("FA7D76C4-580C-4BAF-BA40-C71A01C68478"), 1
    ),
    "reducedtest_underloadreduction_ccs_input41": AreaAnalyzeClass(
        uuid.UUID("D46F4AF4-5942-4611-85D2-A91B9A204522"), 1
    ),
    "reducedtest_underloadreduction_ccs_input42": AreaAnalyzeClass(
        uuid.UUID("C7A129B9-3D49-4F69-835C-E484A195592A"), 1
    ),
    "reducedtest_underloadreduction_ccs_input43": AreaAnalyzeClass(
        uuid.UUID("33A094C2-D327-4FCF-876E-23DEF35B9145"), 1
    ),
    "reducedtest_underloadreduction_ccs_input44": AreaAnalyzeClass(
        uuid.UUID("E81FC0BD-6C96-48E6-956D-6BA3066DA1BD"), 1
    ),
    "reducedtest_underloadreduction_ccs_input45": AreaAnalyzeClass(
        uuid.UUID("EEF2CF0D-5FE2-4D89-B3F9-F553402684EF"), 1
    ),
    "reducedtest_underloadreduction_ccs_input46": AreaAnalyzeClass(
        uuid.UUID("A74B9C52-1500-4E6E-BB1C-016606D29AE9"), 1
    ),
    "reducedtest_underloadreduction_ccs_input47": AreaAnalyzeClass(
        uuid.UUID("60811272-D9AF-484F-BC22-0633113CDEBF"), 1
    ),
    "reducedtest_underloadreduction_ccs_input48": AreaAnalyzeClass(
        uuid.UUID("091CEE27-6142-42B3-8711-7461D613EC2F"), 1
    ),
    "reducedtest_underloadreduction_ccs_input49": AreaAnalyzeClass(
        uuid.UUID("1CE62BA3-47AD-42B4-A90A-FCBE472B9A17"), 1
    ),
    "reducedtest_underloadreduction_ccs_input5": AreaAnalyzeClass(
        uuid.UUID("ECE05955-3D25-493B-836C-0BE4F6EC8EE7"), 1
    ),
    "reducedtest_underloadreduction_ccs_input50": AreaAnalyzeClass(
        uuid.UUID("D3A37449-182C-44E1-AE09-7EC566676D1A"), 1
    ),
    "reducedtest_underloadreduction_ccs_input51": AreaAnalyzeClass(
        uuid.UUID("5A27099F-1526-42CC-8876-5B214216256C"), 1
    ),
    "reducedtest_underloadreduction_ccs_input52": AreaAnalyzeClass(
        uuid.UUID("BB07F956-25FC-43C4-9E3C-049BD5299C77"), 1
    ),
    "reducedtest_underloadreduction_ccs_input53": AreaAnalyzeClass(
        uuid.UUID("77FC98B9-0D62-4EB7-B193-9FC4B7D73213"), 1
    ),
    "reducedtest_underloadreduction_ccs_input54": AreaAnalyzeClass(
        uuid.UUID("157FCAD8-E141-449E-9CC8-B8A1AD7823CC"), 1
    ),
    "reducedtest_underloadreduction_ccs_input55": AreaAnalyzeClass(
        uuid.UUID("F7676B51-9013-443D-B811-953F4CA359EC"), 1
    ),
    "reducedtest_underloadreduction_ccs_input56": AreaAnalyzeClass(
        uuid.UUID("346A4455-60B6-43D4-B600-2B7272A5F183"), 1
    ),
    "reducedtest_underloadreduction_ccs_input57": AreaAnalyzeClass(
        uuid.UUID("CBEFCFA0-EB35-4216-BAA0-531548DFE073"), 1
    ),
    "reducedtest_underloadreduction_ccs_input58": AreaAnalyzeClass(
        uuid.UUID("6636207D-4DF5-44BC-B51C-642B557B63D5"), 1
    ),
    "reducedtest_underloadreduction_ccs_input59": AreaAnalyzeClass(
        uuid.UUID("7F99D0CF-1117-4FBB-B618-C28C22EEA501"), 1
    ),
    "reducedtest_underloadreduction_ccs_input6": AreaAnalyzeClass(
        uuid.UUID("61B5AF20-1435-4D4E-88F4-7F1C1B079E79"), 1
    ),
    "reducedtest_underloadreduction_ccs_input60": AreaAnalyzeClass(
        uuid.UUID("32D36E63-0529-443E-80A5-596702EAF362"), 1
    ),
    "reducedtest_underloadreduction_ccs_input61": AreaAnalyzeClass(
        uuid.UUID("F943C65E-8827-459E-8902-27C3D01A4736"), 1
    ),
    "reducedtest_underloadreduction_ccs_input62": AreaAnalyzeClass(
        uuid.UUID("B207EF25-36CF-467C-BBDE-BDB060E24FF7"), 1
    ),
    "reducedtest_underloadreduction_ccs_input63": AreaAnalyzeClass(
        uuid.UUID("87E46443-CAC4-4480-A846-9D0F5545E549"), 1
    ),
    "reducedtest_underloadreduction_ccs_input64": AreaAnalyzeClass(
        uuid.UUID("D061A4CB-D0FE-4BB0-83EB-36FEBCD9ED2D"), 1
    ),
    "reducedtest_underloadreduction_ccs_input65": AreaAnalyzeClass(
        uuid.UUID("F1F02B69-0BC9-485F-A79D-3C68D7B5E35F"), 1
    ),
    "reducedtest_underloadreduction_ccs_input66": AreaAnalyzeClass(
        uuid.UUID("34F1ADB5-9D92-4334-AFC3-411862BB0A6C"), 1
    ),
    "reducedtest_underloadreduction_ccs_input67": AreaAnalyzeClass(
        uuid.UUID("A1F1EB23-3319-4052-8ABF-E8640A4074AB"), 1
    ),
    "reducedtest_underloadreduction_ccs_input68": AreaAnalyzeClass(
        uuid.UUID("7CC3BB90-DCF8-4D9D-9F85-F01C64440BB6"), 1
    ),
    "reducedtest_underloadreduction_ccs_input69": AreaAnalyzeClass(
        uuid.UUID("A0EE6BF4-A11C-472E-9F1A-CE5A9046D1B3"), 1
    ),
    "reducedtest_underloadreduction_ccs_input7": AreaAnalyzeClass(
        uuid.UUID("0A914B0C-E40D-4460-8E42-5D9AF477510D"), 1
    ),
    "reducedtest_underloadreduction_ccs_input70": AreaAnalyzeClass(
        uuid.UUID("AEB6E10C-804C-4E45-94C4-39FD63EF9317"), 1
    ),
    "reducedtest_underloadreduction_ccs_input71": AreaAnalyzeClass(
        uuid.UUID("65C69106-F34A-4D2B-9C03-58B4CEF69B49"), 1
    ),
    "reducedtest_underloadreduction_ccs_input72": AreaAnalyzeClass(
        uuid.UUID("19F2BF5F-B287-4B94-ACF1-5EB8FEBC57FC"), 1
    ),
    "reducedtest_underloadreduction_ccs_input73": AreaAnalyzeClass(
        uuid.UUID("7CE48203-A07D-4D61-805E-74D7CE0D325F"), 1
    ),
    "reducedtest_underloadreduction_ccs_input74": AreaAnalyzeClass(
        uuid.UUID("AAECF91D-0F77-4566-8F1F-5E3ADB01D85C"), 1
    ),
    "reducedtest_underloadreduction_ccs_input75": AreaAnalyzeClass(
        uuid.UUID("22159284-FC5B-424F-86F5-E8607346160B"), 1
    ),
    "reducedtest_underloadreduction_ccs_input76": AreaAnalyzeClass(
        uuid.UUID("22D447EA-3D9B-4D5E-87F0-D55588570F42"), 1
    ),
    "reducedtest_underloadreduction_ccs_input77": AreaAnalyzeClass(
        uuid.UUID("8272862A-4E5A-481A-8D16-A103D0359118"), 1
    ),
    "reducedtest_underloadreduction_ccs_input78": AreaAnalyzeClass(
        uuid.UUID("EFC9CB24-AB14-43FA-84C6-6CE26D8332E5"), 1
    ),
    "reducedtest_underloadreduction_ccs_input79": AreaAnalyzeClass(
        uuid.UUID("6E2F7800-1579-4AEB-A06D-A346C7A8F989"), 1
    ),
    "reducedtest_underloadreduction_ccs_input8": AreaAnalyzeClass(
        uuid.UUID("E1AB09B5-76CD-4A13-B987-6D1E1A35ED38"), 1
    ),
    "reducedtest_underloadreduction_ccs_input80": AreaAnalyzeClass(
        uuid.UUID("140ADCF6-FEC7-4AFF-8E65-9B00BF87B84F"), 1
    ),
    "reducedtest_underloadreduction_ccs_input81": AreaAnalyzeClass(
        uuid.UUID("24302B80-D110-422A-A434-3FC8A6BADDC1"), 1
    ),
    "reducedtest_underloadreduction_ccs_input82": AreaAnalyzeClass(
        uuid.UUID("5AA161CD-C519-4475-8E04-2002C2C90021"), 1
    ),
    "reducedtest_underloadreduction_ccs_input83": AreaAnalyzeClass(
        uuid.UUID("356F5644-D196-4567-A1A2-08AB1E57DFA7"), 1
    ),
    "reducedtest_underloadreduction_ccs_input84": AreaAnalyzeClass(
        uuid.UUID("A381EB96-4CBB-4FAC-8142-8CC689A20120"), 1
    ),
    "reducedtest_underloadreduction_ccs_input85": AreaAnalyzeClass(
        uuid.UUID("9AC265D1-3064-4553-8A86-91B458EECBE4"), 1
    ),
    "reducedtest_underloadreduction_ccs_input86": AreaAnalyzeClass(
        uuid.UUID("0F0F1ABC-A808-47EB-893A-15C389D99676"), 1
    ),
    "reducedtest_underloadreduction_ccs_input87": AreaAnalyzeClass(
        uuid.UUID("66FC9B34-0F18-4CE4-B361-8A3353357D89"), 1
    ),
    "reducedtest_underloadreduction_ccs_input88": AreaAnalyzeClass(
        uuid.UUID("10218826-F916-4695-B025-411C6BF60E9E"), 1
    ),
    "reducedtest_underloadreduction_ccs_input89": AreaAnalyzeClass(
        uuid.UUID("39F2C54B-52EA-4133-A9E0-A670F790ED72"), 1
    ),
    "reducedtest_underloadreduction_ccs_input9": AreaAnalyzeClass(
        uuid.UUID("77661A35-1525-4291-A44F-3381F5532859"), 1
    ),
    "reducedtest_underloadreduction_ccs_input90": AreaAnalyzeClass(
        uuid.UUID("1E73EBB6-881C-4B2F-83E5-8C1508474DD4"), 1
    ),
    "reducedtest_underloadreduction_ccs_input91": AreaAnalyzeClass(
        uuid.UUID("18CAA1F2-3411-438D-B5D7-FD313C767394"), 1
    ),
    "reducedtest_underloadreduction_ccs_input92": AreaAnalyzeClass(
        uuid.UUID("084ACCBB-47ED-4C66-ACE5-D52C59EBFDBA"), 1
    ),
    "reducedtest_underloadreduction_ccs_input93": AreaAnalyzeClass(
        uuid.UUID("48147AB4-8D19-4D6B-B5C9-0F6B47127D59"), 1
    ),
    "reducedtest_underloadreduction_ccs_input94": AreaAnalyzeClass(
        uuid.UUID("21CAD94F-8002-4881-8FB6-E67E81A78840"), 1
    ),
    "reducedtest_underloadreduction_ccs_input95": AreaAnalyzeClass(
        uuid.UUID("2A551484-8C4D-4087-A4A0-C85F5CB12E31"), 1
    ),
    "reducedtest_underloadreduction_ccs_input96": AreaAnalyzeClass(
        uuid.UUID("44305A8C-2FB5-4961-8B14-A7852C6C2B8E"), 1
    ),
    "reducedtest_underloadreduction_ccs_input97": AreaAnalyzeClass(
        uuid.UUID("570F5999-D49F-4AE3-B018-247D79EEF4E8"), 1
    ),
    "reducedtest_underloadreduction_ccs_input98": AreaAnalyzeClass(
        uuid.UUID("24014BD0-8985-46FA-A95C-7CF42A61F805"), 1
    ),
    "reducedtest_underloadreduction_ccs_input99": AreaAnalyzeClass(
        uuid.UUID("F004B0FA-6F56-4698-8E31-2256B07CBD20"), 1
    ),
    "reducedtest_underloadreduction_ccs_std": AreaAnalyzeClass(
        uuid.UUID("3D09D506-E2FF-4ADA-B7DF-0D9F374A2719"), 2
    ),
    "reducedtest_underloadreduction_cluster2_result": AreaAnalyzeClass(
        uuid.UUID("9B7DFDF3-1DA0-453A-8663-C9EE35F7E57B"), 2
    ),
    "reducedtest_underloadreduction_cluster2_w": AreaAnalyzeClass(
        uuid.UUID("52B12D28-5A9D-4FE3-948E-58CC2372AB5E"), 1
    ),
    "reducedtest_underloadreduction_cluster2_w1": AreaAnalyzeClass(
        uuid.UUID("4743D221-B367-41D5-9A42-A757201D4983"), 1
    ),
    "reducedtest_underloadreduction_cluster5_result": AreaAnalyzeClass(
        uuid.UUID("3C4EFCDA-1407-4778-BE0E-09016CE9AC50"), 2
    ),
    "reducedtest_underloadreduction_cluster5_w": AreaAnalyzeClass(
        uuid.UUID("B0C7D81B-6EF5-4B80-8521-7F8075AE1ED2"), 1
    ),
    "reducedtest_underloadreduction_cluster5_w1": AreaAnalyzeClass(
        uuid.UUID("DA95D1EF-3C53-4D51-A98B-44CB96B2D883"), 1
    ),
    "reducedtest_underloadreduction_fragmention_33563mm": AreaAnalyzeClass(
        uuid.UUID("095816AF-10D6-4852-97EE-6384567561E3"), 1
    ),
    "reducedtest_underloadreduction_fragmention_33563w": AreaAnalyzeClass(
        uuid.UUID("7E6C30BC-6F0E-4A8C-8525-EB9FF596ACC7"), 1
    ),
    "reducedtest_underloadreduction_fragmention_335mm": AreaAnalyzeClass(
        uuid.UUID("5E96D9CB-F21A-432F-8DEE-17FFB4A5C9DD"), 1
    ),
    "reducedtest_underloadreduction_fragmention_335w": AreaAnalyzeClass(
        uuid.UUID("7F80336D-E2E4-4FB0-914A-4BB694496DED"), 1
    ),
    "reducedtest_underloadreduction_fragmention_63mm": AreaAnalyzeClass(
        uuid.UUID("23653EEC-6AE7-48F5-A87A-93126D8E1D84"), 1
    ),
    "reducedtest_underloadreduction_fragmention_63w": AreaAnalyzeClass(
        uuid.UUID("B7547C08-9C63-4241-B24A-14B4942FCFDF"), 1
    ),
    "reducedtest_underloadreduction_fragmention_weight": AreaAnalyzeClass(
        uuid.UUID("05703C84-E3EE-49F7-9372-EDC2CADE78A8"), 1
    ),
    "reducedtest_underloadreduction_mfe_input1": AreaAnalyzeClass(
        uuid.UUID("BBAB6675-66AB-4ACB-A437-FF06BB358598"), 1
    ),
    "reducedtest_underloadreduction_reducibility_feo": AreaAnalyzeClass(
        uuid.UUID("EB735B8B-D941-4471-BD18-A0163AFC766F"), 1
    ),
    "reducedtest_underloadreduction_reducibility_result": AreaAnalyzeClass(
        uuid.UUID("AE868E8E-7D95-4B9C-8381-A5A05B56B40E"), 2
    ),
    "reducedtest_underloadreduction_reducibility_tfe": AreaAnalyzeClass(
        uuid.UUID("45528B04-5B7F-4C8A-B65F-47F3E9CE420E"), 1
    ),
    "reducedtest_underloadreduction_reducibility_wafter": AreaAnalyzeClass(
        uuid.UUID("4232C893-20C5-4D97-9CFE-BC5EAAFBFC46"), 1
    ),
    "reducedtest_underloadreduction_reducibility_wbefore": AreaAnalyzeClass(
        uuid.UUID("17CEE4AB-C336-4613-AD04-A6E405194F2D"), 1
    ),
    "reducedtest_underloadreduction_tfeafter_input": AreaAnalyzeClass(
        uuid.UUID("2C91849B-15EC-4506-8682-CF38C00C9204"), 1
    ),
    "rs_rs1overflow_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("4A97AA4D-C3A3-4215-AD35-3A408D8E1CA3"), 1
    ),
    "rs_rs1overflow_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("2D5B9617-8538-4C7E-B81B-122DFE48FFEC"), 2
    ),
    "rs_rs1overflow_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("EA9B2715-B242-411F-A905-1F21824DE2FC"), 1
    ),
    "rs_rs1overflow_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("1B1C0D05-FDCE-4938-A6F5-4F346AEE6949"), 2
    ),
    "rs_rs1overflow_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("F087EB48-2FBA-4849-BC60-18F541C9990B"), 1
    ),
    "rs_rs1overflow_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("82DE875E-C013-4B5D-B8E1-79C816011813"), 2
    ),
    "rs_rs1overflow_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("9D4B715F-9BF0-4FE7-9211-CFD04444FEF5"), 1
    ),
    "rs_rs1overflow_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("EB9D17A7-16CE-402D-AAFF-D535239C91FB"), 2
    ),
    "rs_rs1overflow_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("37ED1F33-4821-4CBD-A165-4EBBDE05BC79"), 1
    ),
    "rs_rs1overflow_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("3C5EF93D-817A-4100-B6EB-4938EF6EBD37"), 2
    ),
    "rs_rs1overflow_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("BDC48547-D63C-459C-9ADB-BEBB7A2B960D"), 1
    ),
    "rs_rs1product_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("0CBB0E06-977B-4D1B-8A2E-C19C9D789C80"), 1
    ),
    "rs_rs1product_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("02A75C12-6837-4268-98A6-1CC85EEF20C2"), 2
    ),
    "rs_rs1product_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("958A417E-3C2B-45C9-B38E-F6F6A40D0461"), 1
    ),
    "rs_rs1product_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("C68F404D-1F78-449C-82F4-F053CB19F9F6"), 2
    ),
    "rs_rs1product_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("9E86B81F-F39F-44DB-8101-5E4D7EA5EC29"), 1
    ),
    "rs_rs1product_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("C064B320-7756-4A11-B2A9-C566132B58E6"), 2
    ),
    "rs_rs1product_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("FE70ABBA-CF00-4B0D-922E-984E8DF4DD1B"), 1
    ),
    "rs_rs1product_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("034EA11F-DD0F-412D-8B68-95100FE4E5B0"), 2
    ),
    "rs_rs1product_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("822330CE-D1F2-4CAB-877B-AF368957BD94"), 1
    ),
    "rs_rs1product_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("43E68A9B-0234-4061-B1EE-2DF98DC152D9"), 2
    ),
    "rs_rs1product_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("7A3CC6CF-C480-4B9F-95E7-D882C056261A"), 1
    ),
    "rs_rs2overflow_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("BF52DC36-4746-40B4-807A-A315CDF5351E"), 1
    ),
    "rs_rs2overflow_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("9098FAF5-49EB-4C82-BFFC-DB270F4F113D"), 2
    ),
    "rs_rs2overflow_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("AA36BC56-65BD-4747-8E74-AADDE988AD65"), 1
    ),
    "rs_rs2overflow_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("2D1D0E85-D2BE-4FA8-B1A9-3FFEDFA33CA7"), 2
    ),
    "rs_rs2overflow_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("F8910E93-4A7A-4ED4-9BF5-78FAA64A88FC"), 1
    ),
    "rs_rs2overflow_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("CC94213E-B490-4443-8E9F-BF443A094CB9"), 2
    ),
    "rs_rs2overflow_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("18C3D4A2-966D-4758-9980-A9BB9BD38636"), 1
    ),
    "rs_rs2overflow_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("E58DD443-AA61-4A4D-A44C-4B8E00F8DB3A"), 2
    ),
    "rs_rs2overflow_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("593058D6-DB78-43B9-9509-DF1FFE9BF26D"), 1
    ),
    "rs_rs2overflow_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("707CD4D7-95DD-441E-922C-667240205196"), 2
    ),
    "rs_rs2overflow_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("EFAC0516-B8EC-411A-A0DE-CA649AB81B40"), 1
    ),
    "rs_rs2product_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("3C9722C9-3C78-4AA0-948D-14B8D343AB3E"), 1
    ),
    "rs_rs2product_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("F37DBFB0-FA92-4885-B564-E3A08725B44B"), 2
    ),
    "rs_rs2product_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("7EAC020C-4908-4926-B8BF-95A9203B0983"), 1
    ),
    "rs_rs2product_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("3AA27F11-26A9-49AE-8F33-4D58DA39DE61"), 2
    ),
    "rs_rs2product_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("3AB08019-E2B8-4472-A6F4-00C40A6DFD76"), 1
    ),
    "rs_rs2product_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("1C4BED9F-427E-441B-A72D-90BD894BA580"), 2
    ),
    "rs_rs2product_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("FC91E876-D044-4D55-BDF0-DF8F42A22A2E"), 1
    ),
    "rs_rs2product_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("94FA5570-C3E7-42F9-BD14-3538BD92689F"), 2
    ),
    "rs_rs2product_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("1FC1BDBB-572E-44FC-A5EF-B7F305CCA19D"), 1
    ),
    "rs_rs2product_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("8DAC5E7F-887F-4ABF-A6D2-114829019F35"), 2
    ),
    "rs_rs2product_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("6D78067A-BBC0-4C7A-92C9-F56ECA1C6691"), 1
    ),
    "rs_rs3overflow_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("2B5B4AB4-4CF0-45A6-A8AB-D055EBD19389"), 1
    ),
    "rs_rs3overflow_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("7FCA90F8-C266-46F7-BD5C-AD9B6B2A522A"), 2
    ),
    "rs_rs3overflow_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("C80B423B-4B7F-4EF3-B7AC-A2F4DE8A2598"), 1
    ),
    "rs_rs3overflow_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("930F01F9-6E50-4274-9326-260E74F2883A"), 2
    ),
    "rs_rs3overflow_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("5D590673-6292-430A-B77C-63AED5DB4191"), 1
    ),
    "rs_rs3overflow_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("B69C3380-EBB6-441B-A9C3-D48381424849"), 2
    ),
    "rs_rs3overflow_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("B5CCF31F-0583-46D4-BED7-0397EECEDB64"), 1
    ),
    "rs_rs3overflow_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("1112C8B0-BC84-41DA-8D8B-8521FA7F5699"), 2
    ),
    "rs_rs3overflow_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("63CC9923-A795-42D5-B561-1A61263C9719"), 1
    ),
    "rs_rs3overflow_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("029D4208-7CF1-4BA0-936F-8E860A900FAF"), 2
    ),
    "rs_rs3overflow_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("AD6D6E86-7BE2-40F1-99F7-8D7E5F2AC4F5"), 1
    ),
    "rs_rs3product_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("015D196F-8D5F-4B76-9B57-5FCA7EB45125"), 1
    ),
    "rs_rs3product_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("F9BAF9A6-1827-4F04-AFF8-3E6CBE78CDF8"), 2
    ),
    "rs_rs3product_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("6A82959B-2F2C-4C36-AEBE-E42B9562DDB4"), 1
    ),
    "rs_rs3product_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("46585BC6-03EF-48D4-8CB0-506E8E9943EE"), 2
    ),
    "rs_rs3product_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("EAA67660-9AD7-401D-A505-3AFAACE4FBAD"), 1
    ),
    "rs_rs3product_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("7065B775-BB9A-4FD7-965F-AC78BF99E579"), 2
    ),
    "rs_rs3product_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("F4641B4C-7C4B-4A86-9EC0-A0C3445A06DB"), 1
    ),
    "rs_rs3product_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("7FA086CF-BBF7-4F22-8A77-66B77E6E2482"), 2
    ),
    "rs_rs3product_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("79511761-49D9-4DBD-BC6E-0EA6EAEC4A34"), 1
    ),
    "rs_rs3product_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("B7862D4A-796F-4FE7-B7AB-25692CF17C2F"), 2
    ),
    "rs_rs3product_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("83C810C0-FFF8-4178-B6C7-594108559BE6"), 1
    ),
    "rs_rs4overflow_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("B19D3FDF-2ED1-4867-8589-2A9AB71AB864"), 1
    ),
    "rs_rs4overflow_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("6B73E80B-2799-48AC-94EE-78EB40F125CD"), 2
    ),
    "rs_rs4overflow_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("E28437E7-D326-470C-AB7B-1408052E4C25"), 1
    ),
    "rs_rs4overflow_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("984FE835-BF94-4564-B3F5-467C5F09263F"), 2
    ),
    "rs_rs4overflow_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("30C14DF4-E1CB-4D5C-8251-E541B65DC9B2"), 1
    ),
    "rs_rs4overflow_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("93918514-8B79-4468-B75D-A1B49281DEDF"), 2
    ),
    "rs_rs4overflow_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("A34BE4B4-CAA0-4A4F-86B4-06BCB9BE783B"), 1
    ),
    "rs_rs4overflow_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("8B9CDFC4-9E17-4569-B7FF-1F091F3D52A8"), 2
    ),
    "rs_rs4overflow_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("280D739D-E984-4E7D-BE0C-2A65FF970978"), 1
    ),
    "rs_rs4overflow_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("17683AFA-B2DB-4164-AEAB-962D8CB43DEB"), 2
    ),
    "rs_rs4overflow_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("50370903-2A06-45E0-AFDB-DD29FD4EE743"), 1
    ),
    "rs_rs4product_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("5929DC3D-CA19-439E-8E47-754E38277A3A"), 1
    ),
    "rs_rs4product_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("EDE6B1D2-1323-4B89-B477-70547A3F37D3"), 2
    ),
    "rs_rs4product_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("9EF613D3-CA2F-46EE-93CA-1AD8CC735640"), 1
    ),
    "rs_rs4product_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("CCF10DF2-3FE7-41C3-8FAB-643C01AF07B1"), 2
    ),
    "rs_rs4product_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("8BB9137E-A1C9-4CB1-992B-1657D0F83956"), 1
    ),
    "rs_rs4product_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("4A2B2F16-FC1C-4A7F-B841-60C15B65A66E"), 2
    ),
    "rs_rs4product_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("9DB9B229-DB20-466A-9869-8A5B863CA104"), 1
    ),
    "rs_rs4product_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("E6828EAA-2DAC-45F2-AE0E-CA29A9D328AB"), 2
    ),
    "rs_rs4product_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("583FB149-58C9-4FD1-AF01-79EBF5A16529"), 1
    ),
    "rs_rs4product_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("88809511-6D11-48BC-B2B9-7DB1A3F319FD"), 2
    ),
    "rs_rs4product_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("6AA89A8F-3AC9-4DFC-A701-77F0893DC4D4"), 1
    ),
    "rs_rs5overflow_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("D42F1CD5-E2AE-42FB-B82E-2B21D03D193E"), 1
    ),
    "rs_rs5overflow_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("F65366BC-D7E1-4746-860C-21BDD5D4CF26"), 2
    ),
    "rs_rs5overflow_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("B7CDA2EF-D4DE-44C9-9D0B-6D4228D77221"), 1
    ),
    "rs_rs5overflow_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("6EADD344-5D67-4487-9671-7CF94EBF9F35"), 2
    ),
    "rs_rs5overflow_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("139388E4-83A3-4FAA-856C-E5CDAE5F05F6"), 1
    ),
    "rs_rs5overflow_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("D76BD661-D0B0-4841-AA61-A86E0E53BEF5"), 2
    ),
    "rs_rs5overflow_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("67885ECC-D910-49EE-AA15-F5A32B95AC5F"), 1
    ),
    "rs_rs5overflow_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("4B2DE5AE-3B96-4F6B-BA10-EEC0702B5D79"), 2
    ),
    "rs_rs5overflow_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("A25F877D-3B79-4487-A296-ACAEDCB20821"), 1
    ),
    "rs_rs5overflow_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("AA889EC1-22CC-4ACE-AB0D-5ABD8FCD579B"), 2
    ),
    "rs_rs5overflow_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("ECFB9167-30B3-40FF-B859-DB0BAFF50C6A"), 1
    ),
    "rs_rs5product_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("B0435814-59EA-479D-921D-2E07983D4ACC"), 1
    ),
    "rs_rs5product_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("D21FA490-02C8-4D2E-A28A-650AD9756162"), 2
    ),
    "rs_rs5product_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("9836C4D6-CBC0-4495-A281-5FAD26D96CAE"), 1
    ),
    "rs_rs5product_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("FCB729B1-6CF6-4A73-8137-019FED1A70B1"), 2
    ),
    "rs_rs5product_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("BB21D536-B4C5-494B-980B-59639945453F"), 1
    ),
    "rs_rs5product_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("21414EC5-68CA-4AE7-BF29-5E9C841CD73D"), 2
    ),
    "rs_rs5product_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("7B22CE88-4C65-4A99-A7AF-686469045CBD"), 1
    ),
    "rs_rs5product_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("38378C2D-6008-4BDA-A6F7-D61E4AF345E1"), 2
    ),
    "rs_rs5product_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("265B134A-0D36-498E-BA7D-5421E9DB5F24"), 1
    ),
    "rs_rs5product_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("C3DD6677-E94F-415D-B037-19759151CF8F"), 2
    ),
    "rs_rs5product_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("3D8C2FD0-72CA-4958-90DD-2A7C83B7896A"), 1
    ),
    "rs_rs6overflow_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("D7B0F932-6095-4C4A-B796-EE73AECBFCDE"), 1
    ),
    "rs_rs6overflow_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("4159A6EF-2EAF-410A-937D-C793DA559E42"), 2
    ),
    "rs_rs6overflow_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("AEB84FB3-770A-4116-93FB-F5417DD95A1B"), 1
    ),
    "rs_rs6overflow_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("D0A53D48-3045-48A2-8038-04A1642149C6"), 2
    ),
    "rs_rs6overflow_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("7B3C3ED5-C713-4958-ADF5-34D526B525B6"), 1
    ),
    "rs_rs6overflow_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("807260D4-35BD-44BD-AED2-A438BFAC4975"), 2
    ),
    "rs_rs6overflow_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("6A6712C9-2795-42EC-BEBE-0FF1CFBBB3EC"), 1
    ),
    "rs_rs6overflow_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("D9994194-083F-4D53-99E5-449AD7959046"), 2
    ),
    "rs_rs6overflow_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("F250C9E8-B791-4C77-922B-7FAFC5FE413B"), 1
    ),
    "rs_rs6overflow_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("4EDAEF7D-EE4B-4993-86CA-E8891B53B022"), 2
    ),
    "rs_rs6overflow_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("0E8F26B8-FD7F-4C29-BE0D-D6ADC2E97FB4"), 1
    ),
    "rs_rs6product_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("F3E8199B-33EE-4975-AD6D-8A39059F2753"), 1
    ),
    "rs_rs6product_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("D1B16144-4125-4F71-B3D2-CA4B099A9BC9"), 2
    ),
    "rs_rs6product_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("E9A279C4-4A5A-4741-A38E-15FA8B0E65F3"), 1
    ),
    "rs_rs6product_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("117767F3-0D7A-460E-BD69-D69D24BAA435"), 2
    ),
    "rs_rs6product_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("EC406AD2-CD49-41D2-B9A7-2A3FF3B4497D"), 1
    ),
    "rs_rs6product_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("444C38E1-DEB2-4FD2-A660-0F613BC49403"), 2
    ),
    "rs_rs6product_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("D1096688-399E-422F-A592-019DFC69BF70"), 1
    ),
    "rs_rs6product_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("5CF0189D-BF38-48FB-8ACD-39F8A788E8D1"), 2
    ),
    "rs_rs6product_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("47FEF755-F156-424D-B956-090960A78730"), 1
    ),
    "rs_rs6product_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("46EC3AAC-1439-4E4E-84D2-BDA2E2E3F69A"), 2
    ),
    "rs_rs6product_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("C2012A3D-B697-44D5-850C-34D8BF5EE99B"), 1
    ),
    "sludge_sludge_20micron_passing": AreaAnalyzeClass(
        uuid.UUID("22D4CBF2-491D-57F0-94AF-BD93E069AE9A"), 2
    ),
    "sludge_sludge_20micron_wa": AreaAnalyzeClass(
        uuid.UUID("82F1E942-5BD0-5F70-92D9-8B865C2B57A0"), 1
    ),
    "sludge_sludge_20micron_wb": AreaAnalyzeClass(
        uuid.UUID("62E7DD01-36AE-5D9C-BEA3-1F8047E10718"), 1
    ),
    "sludge_sludge_20micron_ws": AreaAnalyzeClass(
        uuid.UUID("7206C53E-02F5-51E7-99D5-C0C371AD815D"), 1
    ),
    "sludge_sludge_25micron_passing": AreaAnalyzeClass(
        uuid.UUID("A2FF2F07-8310-510A-B27E-22A4902C9E82"), 2
    ),
    "sludge_sludge_25micron_wa": AreaAnalyzeClass(
        uuid.UUID("82310872-4F3A-5EC4-80EB-DFF80B38C736"), 1
    ),
    "sludge_sludge_25micron_wb": AreaAnalyzeClass(
        uuid.UUID("A2C4142F-188B-511D-8BDF-410365FC9251"), 1
    ),
    "sludge_sludge_25micron_ws": AreaAnalyzeClass(
        uuid.UUID("92A8460B-E5B0-54F0-836F-44C032AF421F"), 1
    ),
    "sludge_sludge_45micron_passing": AreaAnalyzeClass(
        uuid.UUID("D20863AB-8BC7-5750-B0B6-29D585175882"), 2
    ),
    "sludge_sludge_45micron_wa": AreaAnalyzeClass(
        uuid.UUID("628E8EB6-DCC0-51D8-9ED4-E0BE9DD28C1D"), 1
    ),
    "sludge_sludge_45micron_wb": AreaAnalyzeClass(
        uuid.UUID("5229F692-40BC-533B-8906-BBB39E2A6D26"), 1
    ),
    "sludge_sludge_45micron_ws": AreaAnalyzeClass(
        uuid.UUID("72B15CEC-56A9-5045-9E78-6B8993926D88"), 1
    ),
    "sludge_sludge_atomic_k2o": AreaAnalyzeClass(
        uuid.UUID("42A92AC2-A334-5CC7-A683-C753D5C2E2AD"), 1
    ),
    "sludge_sludge_atomic_na2o": AreaAnalyzeClass(
        uuid.UUID("82CA1E3F-F68B-516D-A77D-C6B2383C7122"), 1
    ),
    "sludge_sludge_blaine_b": AreaAnalyzeClass(
        uuid.UUID("A22177E7-77A6-5FD5-B9D0-5DC0BADBB16A"), 1
    ),
    "sludge_sludge_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("92D979F3-AC48-53FA-8F34-6E0CFF5A4C2B"), 1
    ),
    "sludge_sludge_blaine_e": AreaAnalyzeClass(
        uuid.UUID("E216D093-DD31-598C-8D68-0D3B41DD03C8"), 1
    ),
    "sludge_sludge_blaine_es": AreaAnalyzeClass(
        uuid.UUID("D286DFBB-2A7B-5676-B76C-978403F25042"), 1
    ),
    "sludge_sludge_blaine_p": AreaAnalyzeClass(
        uuid.UUID("9250A349-F13A-5087-85FD-435477018214"), 1
    ),
    "sludge_sludge_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("22FD00A1-BA18-5444-A154-704FC6F844E9"), 1
    ),
    "sludge_sludge_blaine_result": AreaAnalyzeClass(
        uuid.UUID("12511BC1-E3D7-5246-8C41-B28295048A05"), 2
    ),
    "sludge_sludge_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("A2E1D92E-4390-5CDB-8EE0-199A41D984B7"), 1
    ),
    "sludge_sludge_blaine_t": AreaAnalyzeClass(
        uuid.UUID("B2F06F4D-8C0B-5138-AEDE-B82C4845EB0F"), 1
    ),
    "sludge_sludge_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("A29091DC-AE62-5DC4-A054-2CB9A459043D"), 1
    ),
    "sludge_sludge_feo_avg": AreaAnalyzeClass(
        uuid.UUID("2204217F-71B6-568A-86FF-D32620156F2F"), 2
    ),
    "sludge_sludge_feo_input1": AreaAnalyzeClass(
        uuid.UUID("62B2CE9B-1CD0-5A3B-8612-C6658D6C35D8"), 1
    ),
    "sludge_sludge_feo_input2": AreaAnalyzeClass(
        uuid.UUID("72E22D1A-7EF2-5E9F-A5F6-31CED5DF3821"), 1
    ),
    "sludge_sludge_mfe_avg": AreaAnalyzeClass(
        uuid.UUID("82914D1C-C298-4310-8C54-4D7A40F95136"), 1
    ),
    "sludge_sludge_mfe_input1": AreaAnalyzeClass(
        uuid.UUID("19DFC5C1-E209-4F00-B638-E442ABBA7E2C"), 1
    ),
    "sludge_sludge_mfe_input2": AreaAnalyzeClass(
        uuid.UUID("ECE3A846-D6A1-4221-882C-1A4AC6358F1E"), 1
    ),
    "sludge_sludge_moisture_input": AreaAnalyzeClass(
        uuid.UUID("62B4C2EE-B2C7-5F04-9F9B-6CB3DAEAEDFA"), 1
    ),
    "sludge_sludge_sulfur_input": AreaAnalyzeClass(
        uuid.UUID("32EF2600-EBBD-5AC5-84CE-6ECF85A113EE"), 1
    ),
    "sludge_sludge_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("72967A25-3D3C-5EAD-8EF6-42A064A7A1BB"), 2
    ),
    "sludge_sludge_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("B2823EA9-E720-5386-8F09-3355514AE649"), 1
    ),
    "sludge_sludge_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("52D64831-EDD0-5194-A3D7-E0C582E84722"), 1
    ),
    "sludge_sludge_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("E265BDB1-1312-5A40-9FBE-22343725E0CB"), 1
    ),
    "sludge_sludge_xray_cao": AreaAnalyzeClass(
        uuid.UUID("F2EEA092-B12D-5354-8E53-E740C8264CAE"), 1
    ),
    "sludge_sludge_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("12133C9D-2B6F-508F-9148-AF70A30BFEDD"), 1
    ),
    "sludge_sludge_xray_mno": AreaAnalyzeClass(
        uuid.UUID("12E07DD0-FBC0-5F49-BDF3-D2EC947BBC34"), 1
    ),
    "sludge_sludge_xray_p": AreaAnalyzeClass(
        uuid.UUID("52952FD6-C35B-52EF-B9F5-C004F82B3800"), 1
    ),
    "sludge_sludge_xray_result": AreaAnalyzeClass(
        uuid.UUID("E28370CD-6044-57DE-AC73-267D309C7FB8"), 2
    ),
    "sludge_sludge_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("A2BC34E4-0152-543A-9439-F94A8B22287F"), 1
    ),
    "sludge_sludge_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("929904C8-0801-50D7-88D4-41B46A83EFDB"), 1
    ),
    "unknown_bentonite_45micron_passing": AreaAnalyzeClass(
        uuid.UUID("720B028A-A382-4B31-A783-FB1BC38257D4"), 2
    ),
    "unknown_bentonite_45micron_wa": AreaAnalyzeClass(
        uuid.UUID("1D0D56A0-300C-40D7-BF51-8B0227859AFC"), 1
    ),
    "unknown_bentonite_45micron_wb": AreaAnalyzeClass(
        uuid.UUID("FA92CCF1-4BC6-443E-97B3-BD2DE745D856"), 1
    ),
    "unknown_bentonite_45micron_ws": AreaAnalyzeClass(
        uuid.UUID("F9C8B127-75D3-4123-AB26-516C6E901212"), 1
    ),
    "unknown_bentonite_loi_input": AreaAnalyzeClass(
        uuid.UUID("9C61A700-98CD-41EF-A282-E2333F2FB49E"), 2
    ),
    "unknown_bentonite_moisture_input": AreaAnalyzeClass(
        uuid.UUID("6F8DEB0C-9D57-4CA7-93C1-400B75BA699B"), 1
    ),
    "unknown_bentonite_waterabsorption_k": AreaAnalyzeClass(
        uuid.UUID("48539762-C84E-4651-928A-E7041E5EFB04"), 1
    ),
    "unknown_bentonite_waterabsorption_result": AreaAnalyzeClass(
        uuid.UUID("E0E20361-BC9B-4510-B2B6-D605CF9519E6"), 1
    ),
    "unknown_bentonite_waterabsorption_t1": AreaAnalyzeClass(
        uuid.UUID("F28A0AF2-852D-48D4-AB80-BA15F0BC73CC"), 1
    ),
    "unknown_bentonite_waterabsorption_t2": AreaAnalyzeClass(
        uuid.UUID("54A0FAF7-FEDD-451F-8245-F1E4334C9A0B"), 1
    ),
    "unknown_bentonite_waterabsorption_tr": AreaAnalyzeClass(
        uuid.UUID("F6807FAE-64F9-4111-A5A6-BAC1EF729528"), 1
    ),
    "unknown_bentonite_waterabsorption_w0": AreaAnalyzeClass(
        uuid.UUID("7E2459F5-2269-4F73-9974-61AAC69EE13A"), 1
    ),
    "unknown_bentonite_waterabsorption_w1": AreaAnalyzeClass(
        uuid.UUID("9925B0AC-C846-4EA1-88AD-75D1454668EB"), 1
    ),
    "unknown_bentonite_waterabsorption_w2": AreaAnalyzeClass(
        uuid.UUID("7A10775D-51E8-47A9-8AA0-61C88CD460A1"), 1
    ),
    "unknown_bentonite_waterabsorption2_k": AreaAnalyzeClass(
        uuid.UUID("86BF53EB-9590-479E-88C5-CBC972D238BE"), 1
    ),
    "unknown_bentonite_waterabsorption2_result": AreaAnalyzeClass(
        uuid.UUID("82278D56-9618-4DA1-898F-28EB22C004F1"), 2
    ),
    "unknown_bentonite_waterabsorption2_t1": AreaAnalyzeClass(
        uuid.UUID("419C2628-EED9-4EA9-9F84-8D4634C648B5"), 1
    ),
    "unknown_bentonite_waterabsorption2_t2": AreaAnalyzeClass(
        uuid.UUID("E6BC1BD6-98F3-469A-B555-15B3FD3DD2A0"), 1
    ),
    "unknown_bentonite_waterabsorption2_tr": AreaAnalyzeClass(
        uuid.UUID("92CD7E1E-D913-4942-9407-1C6417C59B8F"), 1
    ),
    "unknown_bentonite_waterabsorption2_w0": AreaAnalyzeClass(
        uuid.UUID("22EA0DFC-78AD-4B90-BB76-A28D63C673FA"), 1
    ),
    "unknown_bentonite_waterabsorption2_w1": AreaAnalyzeClass(
        uuid.UUID("25187803-9E66-4028-B123-5728FD19C01C"), 1
    ),
    "unknown_bentonite_waterabsorption2_w2": AreaAnalyzeClass(
        uuid.UUID("8C41DF09-83CD-40B7-B560-0200F341BE2F"), 1
    ),
    "unknown_bentonite_waterabsorption3_k": AreaAnalyzeClass(
        uuid.UUID("732CC9C7-34B5-4B23-BD31-8460D23AFE7C"), 1
    ),
    "unknown_bentonite_waterabsorption3_result": AreaAnalyzeClass(
        uuid.UUID("90757720-4B44-4B51-8B35-B74D7A004764"), 2
    ),
    "unknown_bentonite_waterabsorption3_t1": AreaAnalyzeClass(
        uuid.UUID("D44980C5-2529-41EC-A5F3-86FE95F35D27"), 1
    ),
    "unknown_bentonite_waterabsorption3_t2": AreaAnalyzeClass(
        uuid.UUID("20F83E0C-89AE-40CB-B55E-B33090C0CCDA"), 1
    ),
    "unknown_bentonite_waterabsorption3_tr": AreaAnalyzeClass(
        uuid.UUID("21E30F10-2910-42E3-A60A-EF1BE955F857"), 1
    ),
    "unknown_bentonite_waterabsorption3_w0": AreaAnalyzeClass(
        uuid.UUID("BFE61C76-E64E-48FF-88B9-473973D6D85C"), 1
    ),
    "unknown_bentonite_waterabsorption3_w1": AreaAnalyzeClass(
        uuid.UUID("FD8F9425-98EA-48E3-B165-DB543B2E7885"), 1
    ),
    "unknown_bentonite_waterabsorption3_w2": AreaAnalyzeClass(
        uuid.UUID("3909606E-3CD7-4A63-8B5D-CFB904688426"), 1
    ),
    "unknown_bentonite_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("3EC7364D-D511-4F86-8A79-3B87EA8F6336"), 1
    ),
    "unknown_bentonite_xray_cao": AreaAnalyzeClass(
        uuid.UUID("175FBF90-3CA8-406A-BE8E-0E3017BA3040"), 1
    ),
    "unknown_bentonite_xray_fe": AreaAnalyzeClass(
        uuid.UUID("2B032A96-D209-4BA3-9701-594A691217BF"), 1
    ),
    "unknown_bentonite_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("EFE547D8-37F8-41A8-8684-BACD0BF4EA62"), 1
    ),
    "unknown_bentonite_xray_mno": AreaAnalyzeClass(
        uuid.UUID("0B261D76-D0D2-40B9-9080-1C63C1EFBE15"), 1
    ),
    "unknown_bentonite_xray_p": AreaAnalyzeClass(
        uuid.UUID("6EE6F0F8-51F7-460C-801F-4BC4D5788629"), 1
    ),
    "unknown_bentonite_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("5E4D831A-6703-4BBF-A2E7-9D4DCFE5FB0D"), 1
    ),
    "unknown_bentonite_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("8122C308-ED5E-4931-929D-99762626D76A"), 1
    ),
    "unknown_concentrate_20micron_passing": AreaAnalyzeClass(
        uuid.UUID("7DA293E2-CE33-40AC-B538-DB8660F7D94C"), 2
    ),
    "unknown_concentrate_20micron_wa": AreaAnalyzeClass(
        uuid.UUID("783EC5A8-4B54-4242-B7FA-D2F537C4C50D"), 1
    ),
    "unknown_concentrate_20micron_wb": AreaAnalyzeClass(
        uuid.UUID("74038974-20B7-4AE1-B685-A832E788218C"), 1
    ),
    "unknown_concentrate_20micron_ws": AreaAnalyzeClass(
        uuid.UUID("4405F10E-4D1B-4408-9780-6EA897C5DCCA"), 1
    ),
    "unknown_concentrate_25micron_passing": AreaAnalyzeClass(
        uuid.UUID("A3F28396-65F8-4F79-8DBB-E18A4F4B6AF4"), 2
    ),
    "unknown_concentrate_25micron_wa": AreaAnalyzeClass(
        uuid.UUID("3302D8CF-3054-4AF7-955D-9BA0DE4B3434"), 1
    ),
    "unknown_concentrate_25micron_wb": AreaAnalyzeClass(
        uuid.UUID("077BBC4F-4A14-4E14-B627-0480436DB505"), 1
    ),
    "unknown_concentrate_25micron_ws": AreaAnalyzeClass(
        uuid.UUID("9BFE8FEC-D439-4134-8B51-D428BD4E300D"), 1
    ),
    "unknown_concentrate_45micron_passing": AreaAnalyzeClass(
        uuid.UUID("20F1ADAF-3A75-480B-9F89-77097F5E84F6"), 2
    ),
    "unknown_concentrate_45micron_wa": AreaAnalyzeClass(
        uuid.UUID("486C8050-5FD1-4F99-A4F3-4C626A723B57"), 1
    ),
    "unknown_concentrate_45micron_wb": AreaAnalyzeClass(
        uuid.UUID("0C220315-B2EB-417D-B9B8-D7D9F2E88E42"), 1
    ),
    "unknown_concentrate_45micron_ws": AreaAnalyzeClass(
        uuid.UUID("BA29CD02-5A45-4546-9305-DF6A3F82DB3F"), 1
    ),
    "unknown_concentrate_atomic_k2o": AreaAnalyzeClass(
        uuid.UUID("B137F9B3-8BAE-4E4C-933C-703C6825A250"), 1
    ),
    "unknown_concentrate_atomic_na2o": AreaAnalyzeClass(
        uuid.UUID("5FF459F8-6B00-4D5D-9E38-D6DB68ACA4C5"), 1
    ),
    "unknown_concentrate_blaine_b": AreaAnalyzeClass(
        uuid.UUID("B94D4650-0590-454E-A022-794E0B2AA9E1"), 1
    ),
    "unknown_concentrate_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("B3640525-2D5D-452C-AF0B-9DDF332231CB"), 1
    ),
    "unknown_concentrate_blaine_e": AreaAnalyzeClass(
        uuid.UUID("335B27C0-AAC1-42EC-A214-19847A835DF5"), 1
    ),
    "unknown_concentrate_blaine_es": AreaAnalyzeClass(
        uuid.UUID("D93EC328-25F6-456B-87D6-58C609D4DD02"), 1
    ),
    "unknown_concentrate_blaine_p": AreaAnalyzeClass(
        uuid.UUID("9E54CB85-97BC-4813-8FD7-D9B8D917C097"), 1
    ),
    "unknown_concentrate_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("51B90FD5-B64F-45C8-A841-00BA6C86A9A3"), 1
    ),
    "unknown_concentrate_blaine_result": AreaAnalyzeClass(
        uuid.UUID("8BA65DE7-30E9-4AEE-A031-44B214FCF08C"), 2
    ),
    "unknown_concentrate_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("0C97B22B-1E31-4EE2-B580-D854C218DC76"), 1
    ),
    "unknown_concentrate_blaine_t": AreaAnalyzeClass(
        uuid.UUID("21146AEC-A4B6-408B-889E-2391CC6A709C"), 1
    ),
    "unknown_concentrate_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("A30C9D1C-54C7-4CB3-B209-2784BC391FBF"), 1
    ),
    "unknown_concentrate_feo_avg": AreaAnalyzeClass(
        uuid.UUID("104F38A4-1D2D-4935-AC6B-CC3A7822727F"), 2
    ),
    "unknown_concentrate_feo_input1": AreaAnalyzeClass(
        uuid.UUID("F4665561-C366-48AF-B455-6E0B497F8D39"), 1
    ),
    "unknown_concentrate_feo_input2": AreaAnalyzeClass(
        uuid.UUID("34EDBE17-B462-464C-BA8C-1FAD54AF88E1"), 1
    ),
    "unknown_concentrate_moisture_input": AreaAnalyzeClass(
        uuid.UUID("30556F53-14CB-4C15-8EE8-F507FAFC606B"), 1
    ),
    "unknown_concentrate_sulfur_input": AreaAnalyzeClass(
        uuid.UUID("C5B5F8F9-9523-4277-8EE7-AE4393C97339"), 1
    ),
    "unknown_concentrate_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("5609D369-0CAE-4ABB-96D9-C01DBD44D2F1"), 2
    ),
    "unknown_concentrate_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("749BE085-6854-40F6-A43F-43C78DFF8DA2"), 1
    ),
    "unknown_concentrate_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("5408197B-EFD8-48D1-9E98-7BA4EFB35537"), 1
    ),
    "unknown_concentrate_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("0C8D46DC-CD51-421F-BF3E-489CCC84E090"), 1
    ),
    "unknown_concentrate_xray_cao": AreaAnalyzeClass(
        uuid.UUID("29E105F1-080A-4BF9-B808-C049080857C6"), 1
    ),
    "unknown_concentrate_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("5BC99238-680C-441F-8B2E-9362B27E0DF5"), 1
    ),
    "unknown_concentrate_xray_mno": AreaAnalyzeClass(
        uuid.UUID("127A983A-18E3-4E0C-A0DE-1B38EA132E87"), 1
    ),
    "unknown_concentrate_xray_p": AreaAnalyzeClass(
        uuid.UUID("521EB80C-01E1-4050-B872-1FAC6051EBF5"), 1
    ),
    "unknown_concentrate_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("FF3C1EDC-7823-4CDE-9921-2134C0B7ABA3"), 1
    ),
    "unknown_concentrate_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("468CC5D3-C7C1-4C2B-AADF-8264CD1A61C6"), 1
    ),
    "unknown_limestone_cao_input": AreaAnalyzeClass(
        uuid.UUID("BEB21F06-1940-4508-99AE-94C9F30237F3"), 2
    ),
    "unknown_limestone_loi_input": AreaAnalyzeClass(
        uuid.UUID("E56E4AC4-5A62-4F2A-BD8E-A4B4B94C7014"), 2
    ),
    "unknown_limestone_mgo_input": AreaAnalyzeClass(
        uuid.UUID("06F5E552-5F81-46D3-9677-8C4833C34D1D"), 2
    ),
    "unknown_limestone_moisture_input": AreaAnalyzeClass(
        uuid.UUID("34F1ECAC-BEE5-468C-9E9D-BA96D39D7CE4"), 1
    ),
    "unknown_limestone_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("3CD3088B-CD0B-44B8-949E-100C72AAC9A5"), 1
    ),
    "unknown_limestone_xray_cao": AreaAnalyzeClass(
        uuid.UUID("44B92D56-727C-4C40-BE1C-1BE27B1ABBF6"), 1
    ),
    "unknown_limestone_xray_fe": AreaAnalyzeClass(
        uuid.UUID("4E1CFA35-8ADB-4B44-9BCD-1946133C8CA4"), 1
    ),
    "unknown_limestone_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("BDD3C2FC-C142-453F-9FBF-826A4D74417C"), 1
    ),
    "unknown_limestone_xray_mno": AreaAnalyzeClass(
        uuid.UUID("4105CB0E-C1D0-475A-AECB-0B5BFE3AD78D"), 1
    ),
    "unknown_limestone_xray_p": AreaAnalyzeClass(
        uuid.UUID("FA5B1707-5ED8-42B0-94F7-813BA2C1E335"), 1
    ),
    "unknown_limestone_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("50E6A4EA-D043-4F31-AAE7-2BDD971852CD"), 1
    ),
    "unknown_limestone_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("1E37F1EC-7FA7-4266-8255-F68D920A81E7"), 1
    ),
    "unknown_pellet_atomic_k2o": AreaAnalyzeClass(
        uuid.UUID("DC12E75E-1D95-4A51-B061-6218E1D42E0B"), 1
    ),
    "unknown_pellet_atomic_na2o": AreaAnalyzeClass(
        uuid.UUID("FD1FCF21-C252-431F-9DC8-6215FA53242B"), 1
    ),
    "unknown_pellet_ccs_100": AreaAnalyzeClass(
        uuid.UUID("30E33E9F-0DD3-4E94-A154-628053F28EBB"), 2
    ),
    "unknown_pellet_ccs_150": AreaAnalyzeClass(
        uuid.UUID("CB4887AE-C0CE-4655-B435-62F99B93042B"), 2
    ),
    "unknown_pellet_ccs_50": AreaAnalyzeClass(
        uuid.UUID("34F4F9A3-2469-43AE-8749-2DDBAF01A5F5"), 2
    ),
    "unknown_pellet_ccs_avg": AreaAnalyzeClass(
        uuid.UUID("77127419-D5B5-47BD-B0C8-6213C2A24C6B"), 2
    ),
    "unknown_pellet_ccs_description": AreaAnalyzeClass(
        uuid.UUID("D7AD221D-544A-4244-B9AC-6224990E7E9B"), 1
    ),
    "unknown_pellet_ccs_input1": AreaAnalyzeClass(
        uuid.UUID("0EB2DB94-57DE-40D1-9076-624EE42D760B"), 1
    ),
    "unknown_pellet_ccs_input10": AreaAnalyzeClass(
        uuid.UUID("0CB341B9-3646-4FFA-A0AE-6272ED8C050B"), 1
    ),
    "unknown_pellet_ccs_input100": AreaAnalyzeClass(
        uuid.UUID("AEA08EE3-8A28-4261-B57D-D9A6F97D8803"), 1
    ),
    "unknown_pellet_ccs_input11": AreaAnalyzeClass(
        uuid.UUID("8C40BF5B-BE58-434E-B29B-62598810B5BB"), 1
    ),
    "unknown_pellet_ccs_input12": AreaAnalyzeClass(
        uuid.UUID("C5784249-C21A-461D-9479-62FBF368567B"), 1
    ),
    "unknown_pellet_ccs_input13": AreaAnalyzeClass(
        uuid.UUID("5FF7106A-9AC7-4B37-92D9-6254972AF5DB"), 1
    ),
    "unknown_pellet_ccs_input14": AreaAnalyzeClass(
        uuid.UUID("F7223CC6-F4F2-432C-8155-62560112356B"), 1
    ),
    "unknown_pellet_ccs_input15": AreaAnalyzeClass(
        uuid.UUID("F557BA22-E3E3-4A59-8381-62D0E10BFABB"), 1
    ),
    "unknown_pellet_ccs_input16": AreaAnalyzeClass(
        uuid.UUID("55830BC7-D628-49C7-B484-6295CD4206DB"), 1
    ),
    "unknown_pellet_ccs_input17": AreaAnalyzeClass(
        uuid.UUID("778AD458-FF65-45D5-B14D-62FCC1E2420B"), 1
    ),
    "unknown_pellet_ccs_input18": AreaAnalyzeClass(
        uuid.UUID("9BE0B528-7707-491D-A81C-6291CD15150B"), 1
    ),
    "unknown_pellet_ccs_input19": AreaAnalyzeClass(
        uuid.UUID("2B519C86-7CE9-4E9F-996A-62F14B24C63B"), 1
    ),
    "unknown_pellet_ccs_input2": AreaAnalyzeClass(
        uuid.UUID("53FF0F00-676E-40A7-90E8-627B5582ED0B"), 1
    ),
    "unknown_pellet_ccs_input20": AreaAnalyzeClass(
        uuid.UUID("A58A15A5-48E3-4551-8427-62B7E4D2226B"), 1
    ),
    "unknown_pellet_ccs_input21": AreaAnalyzeClass(
        uuid.UUID("870B68D6-5EB3-422F-A147-625E594BE91B"), 1
    ),
    "unknown_pellet_ccs_input22": AreaAnalyzeClass(
        uuid.UUID("BF9748F6-8EEA-4B17-9D7B-6247FCB6781B"), 1
    ),
    "unknown_pellet_ccs_input23": AreaAnalyzeClass(
        uuid.UUID("E4DF41F6-162F-428D-8E0C-62420C76669B"), 1
    ),
    "unknown_pellet_ccs_input24": AreaAnalyzeClass(
        uuid.UUID("810673A6-54BA-4B6E-BA78-62458E2DAC6B"), 1
    ),
    "unknown_pellet_ccs_input25": AreaAnalyzeClass(
        uuid.UUID("C3C80F6E-0038-458D-8F5C-6260F945E59B"), 1
    ),
    "unknown_pellet_ccs_input26": AreaAnalyzeClass(
        uuid.UUID("099E62B2-5A85-45B7-96A9-62F57137487B"), 1
    ),
    "unknown_pellet_ccs_input27": AreaAnalyzeClass(
        uuid.UUID("12CC4E53-FF3B-4425-838F-629A5B5E17CB"), 1
    ),
    "unknown_pellet_ccs_input28": AreaAnalyzeClass(
        uuid.UUID("6658CFF4-3C86-4D94-A7C7-620EEDBF972B"), 1
    ),
    "unknown_pellet_ccs_input29": AreaAnalyzeClass(
        uuid.UUID("73FE2BEE-1159-49D8-A9D2-62A9695D965B"), 1
    ),
    "unknown_pellet_ccs_input3": AreaAnalyzeClass(
        uuid.UUID("FB87C66A-83F2-405F-A27A-6279BB539FEB"), 1
    ),
    "unknown_pellet_ccs_input30": AreaAnalyzeClass(
        uuid.UUID("C27625AD-F91D-4166-91FE-62C2C80BC28B"), 1
    ),
    "unknown_pellet_ccs_input31": AreaAnalyzeClass(
        uuid.UUID("A7D2C7F5-1452-4BEE-9A77-1803852F579D"), 1
    ),
    "unknown_pellet_ccs_input32": AreaAnalyzeClass(
        uuid.UUID("64BFA089-1465-4216-B959-14190DED7742"), 1
    ),
    "unknown_pellet_ccs_input33": AreaAnalyzeClass(
        uuid.UUID("F0AD93FD-615A-450E-BEE9-80CA6EEE503C"), 1
    ),
    "unknown_pellet_ccs_input34": AreaAnalyzeClass(
        uuid.UUID("6977CE0D-B58B-4A8D-A9CD-01ED20C3BF89"), 1
    ),
    "unknown_pellet_ccs_input35": AreaAnalyzeClass(
        uuid.UUID("C5BEC143-A054-4641-B491-5507173E116A"), 1
    ),
    "unknown_pellet_ccs_input36": AreaAnalyzeClass(
        uuid.UUID("2DB488C9-4635-4615-8F2B-8BD899BED030"), 1
    ),
    "unknown_pellet_ccs_input37": AreaAnalyzeClass(
        uuid.UUID("86CB9BE9-1F9C-4827-86E4-8ED73C050923"), 1
    ),
    "unknown_pellet_ccs_input38": AreaAnalyzeClass(
        uuid.UUID("FDE55143-1B70-4EC5-93A9-8EE82B281F67"), 1
    ),
    "unknown_pellet_ccs_input39": AreaAnalyzeClass(
        uuid.UUID("27B1F374-3DC5-4CDF-8960-D63BC2380EAC"), 1
    ),
    "unknown_pellet_ccs_input4": AreaAnalyzeClass(
        uuid.UUID("3DEE0F42-A37B-4502-87FC-6218AA246F0B"), 1
    ),
    "unknown_pellet_ccs_input40": AreaAnalyzeClass(
        uuid.UUID("3E408AEB-47A5-4C6B-8D1E-BCF63559E69C"), 1
    ),
    "unknown_pellet_ccs_input41": AreaAnalyzeClass(
        uuid.UUID("AD7FEAC7-8A14-4F98-8538-781ACDCC087C"), 1
    ),
    "unknown_pellet_ccs_input42": AreaAnalyzeClass(
        uuid.UUID("41FEFD61-848D-4A5B-9B69-FAF5A511A5CD"), 1
    ),
    "unknown_pellet_ccs_input43": AreaAnalyzeClass(
        uuid.UUID("2A92F262-DCFB-4921-9B1E-A603B45BF346"), 1
    ),
    "unknown_pellet_ccs_input44": AreaAnalyzeClass(
        uuid.UUID("F693F1A3-3841-4D38-8F4F-30C149D11086"), 1
    ),
    "unknown_pellet_ccs_input45": AreaAnalyzeClass(
        uuid.UUID("4A094C4A-F6C8-4CFD-BE45-91D62B1BCF1D"), 1
    ),
    "unknown_pellet_ccs_input46": AreaAnalyzeClass(
        uuid.UUID("B3A7E219-1051-4280-9ADC-4077FBBE59F4"), 1
    ),
    "unknown_pellet_ccs_input47": AreaAnalyzeClass(
        uuid.UUID("2346AE7F-04B7-40AD-839B-01F5674581DA"), 1
    ),
    "unknown_pellet_ccs_input48": AreaAnalyzeClass(
        uuid.UUID("18275113-DC1A-42E0-9C29-348946AC0416"), 1
    ),
    "unknown_pellet_ccs_input49": AreaAnalyzeClass(
        uuid.UUID("D65A7EF1-F655-473D-B682-FEAE77269FFE"), 1
    ),
    "unknown_pellet_ccs_input5": AreaAnalyzeClass(
        uuid.UUID("C4B1A624-0006-4169-8B08-6272926F5F1B"), 1
    ),
    "unknown_pellet_ccs_input50": AreaAnalyzeClass(
        uuid.UUID("5E51E7CA-94BA-4A15-874F-D9A3E7576694"), 1
    ),
    "unknown_pellet_ccs_input51": AreaAnalyzeClass(
        uuid.UUID("D49C3C0A-B273-4A9E-9A2C-C016B9928D06"), 1
    ),
    "unknown_pellet_ccs_input52": AreaAnalyzeClass(
        uuid.UUID("5F9A6C5E-3DFE-4B78-9289-56A1C638A934"), 1
    ),
    "unknown_pellet_ccs_input53": AreaAnalyzeClass(
        uuid.UUID("F5EF5914-B1AF-4349-91DF-96187CCFEB9E"), 1
    ),
    "unknown_pellet_ccs_input54": AreaAnalyzeClass(
        uuid.UUID("84A39A4B-2621-46B6-9CD0-349F7F9B39E9"), 1
    ),
    "unknown_pellet_ccs_input55": AreaAnalyzeClass(
        uuid.UUID("22EDF209-CEA9-4FC3-A0C8-21D4A1F17B65"), 1
    ),
    "unknown_pellet_ccs_input56": AreaAnalyzeClass(
        uuid.UUID("F31D53E4-EDC7-409E-BFD8-534129165A73"), 1
    ),
    "unknown_pellet_ccs_input57": AreaAnalyzeClass(
        uuid.UUID("900E1F76-3D6F-4E64-ABFB-04DFE46DC39B"), 1
    ),
    "unknown_pellet_ccs_input58": AreaAnalyzeClass(
        uuid.UUID("5743729A-F663-41D7-80FD-7C4EE553DC20"), 1
    ),
    "unknown_pellet_ccs_input59": AreaAnalyzeClass(
        uuid.UUID("EC4CC381-809C-40A8-B058-A7ADE486A9CB"), 1
    ),
    "unknown_pellet_ccs_input6": AreaAnalyzeClass(
        uuid.UUID("78F6444E-C943-4E35-8807-62DD2307CC9B"), 1
    ),
    "unknown_pellet_ccs_input60": AreaAnalyzeClass(
        uuid.UUID("5BB8442C-FA90-4588-AEE5-2F4A278DECFB"), 1
    ),
    "unknown_pellet_ccs_input61": AreaAnalyzeClass(
        uuid.UUID("D832FC66-B334-42F1-B58A-15DF48F33D91"), 1
    ),
    "unknown_pellet_ccs_input62": AreaAnalyzeClass(
        uuid.UUID("2B243AAC-B304-4246-B5E5-2E2D2051D1E3"), 1
    ),
    "unknown_pellet_ccs_input63": AreaAnalyzeClass(
        uuid.UUID("7668B15D-B81B-4454-9C45-B932E827F60E"), 1
    ),
    "unknown_pellet_ccs_input64": AreaAnalyzeClass(
        uuid.UUID("DD91D910-70A1-4344-AFCA-CF1CF449FAA5"), 1
    ),
    "unknown_pellet_ccs_input65": AreaAnalyzeClass(
        uuid.UUID("3E5CF493-7CEA-4014-A215-22E2F812D944"), 1
    ),
    "unknown_pellet_ccs_input66": AreaAnalyzeClass(
        uuid.UUID("48C605B5-8F1E-46F7-97F9-B47DE2C8AFED"), 1
    ),
    "unknown_pellet_ccs_input67": AreaAnalyzeClass(
        uuid.UUID("184D1A8C-799A-4950-B4E5-D987E35B9C91"), 1
    ),
    "unknown_pellet_ccs_input68": AreaAnalyzeClass(
        uuid.UUID("987AEC3A-CCF3-4E1C-A396-77BFED9EB33B"), 1
    ),
    "unknown_pellet_ccs_input69": AreaAnalyzeClass(
        uuid.UUID("50638F29-0DBB-4C16-9BDA-9FCF33460B11"), 1
    ),
    "unknown_pellet_ccs_input7": AreaAnalyzeClass(
        uuid.UUID("E5AC15FA-5570-4D17-A857-6271E7C2823B"), 1
    ),
    "unknown_pellet_ccs_input70": AreaAnalyzeClass(
        uuid.UUID("2E4A3982-8E58-4740-8B7E-5AD5ED792D6B"), 1
    ),
    "unknown_pellet_ccs_input71": AreaAnalyzeClass(
        uuid.UUID("F09031A9-7D0B-434D-B4A4-C98DA6437D93"), 1
    ),
    "unknown_pellet_ccs_input72": AreaAnalyzeClass(
        uuid.UUID("95F9BA00-3CCB-4C23-9183-C20AE728D7C9"), 1
    ),
    "unknown_pellet_ccs_input73": AreaAnalyzeClass(
        uuid.UUID("053C8DA7-32FB-4C86-A24A-D2A7B25A87C5"), 1
    ),
    "unknown_pellet_ccs_input74": AreaAnalyzeClass(
        uuid.UUID("206959B1-075E-4EE0-A18E-AAE5841DB83E"), 1
    ),
    "unknown_pellet_ccs_input75": AreaAnalyzeClass(
        uuid.UUID("C5256A3B-91FF-470A-AF20-FC33AF659A64"), 1
    ),
    "unknown_pellet_ccs_input76": AreaAnalyzeClass(
        uuid.UUID("574A6D66-B1DB-4BE7-8C56-768CE1311C0F"), 1
    ),
    "unknown_pellet_ccs_input77": AreaAnalyzeClass(
        uuid.UUID("0AF2CF7C-0AEC-4193-B26C-C0878B7CBF16"), 1
    ),
    "unknown_pellet_ccs_input78": AreaAnalyzeClass(
        uuid.UUID("B178569B-E135-48BD-9240-A2C6A467FB44"), 1
    ),
    "unknown_pellet_ccs_input79": AreaAnalyzeClass(
        uuid.UUID("5415D622-3CD6-4BE0-9F7D-01F4A981F57F"), 1
    ),
    "unknown_pellet_ccs_input8": AreaAnalyzeClass(
        uuid.UUID("3DD53DCB-6D47-4A42-8E78-6EE629F23075"), 1
    ),
    "unknown_pellet_ccs_input80": AreaAnalyzeClass(
        uuid.UUID("CD1ADA52-5156-4FFB-A08C-A9D5DB4C8AE0"), 1
    ),
    "unknown_pellet_ccs_input81": AreaAnalyzeClass(
        uuid.UUID("80F15B0C-F89B-46CD-96A1-3DBBD44E61AA"), 1
    ),
    "unknown_pellet_ccs_input82": AreaAnalyzeClass(
        uuid.UUID("9B97F474-26E3-4666-93E3-1DAF9095BD6D"), 1
    ),
    "unknown_pellet_ccs_input83": AreaAnalyzeClass(
        uuid.UUID("980AFD64-684F-4D4D-BD78-65324E88C4A6"), 1
    ),
    "unknown_pellet_ccs_input84": AreaAnalyzeClass(
        uuid.UUID("A3F1EA9C-8F4D-470C-97D2-B7AFDD4C7DB7"), 1
    ),
    "unknown_pellet_ccs_input85": AreaAnalyzeClass(
        uuid.UUID("8A8B5820-8A52-4D96-8713-CA968D1D3C6D"), 1
    ),
    "unknown_pellet_ccs_input86": AreaAnalyzeClass(
        uuid.UUID("FCABFEEC-FF7D-420D-8F57-59B3E57E7064"), 1
    ),
    "unknown_pellet_ccs_input87": AreaAnalyzeClass(
        uuid.UUID("7B22A799-E9B7-4119-9041-D0EEB1DB227A"), 1
    ),
    "unknown_pellet_ccs_input88": AreaAnalyzeClass(
        uuid.UUID("2403B99D-BBCF-45BA-9EAF-F3B5E2EE75AB"), 1
    ),
    "unknown_pellet_ccs_input89": AreaAnalyzeClass(
        uuid.UUID("8804B649-A1AE-48FF-AE44-F3930B4D30C2"), 1
    ),
    "unknown_pellet_ccs_input9": AreaAnalyzeClass(
        uuid.UUID("D6DF45E1-44E5-4DAB-A6CA-62D0737397CB"), 1
    ),
    "unknown_pellet_ccs_input90": AreaAnalyzeClass(
        uuid.UUID("86C3F097-E2D9-4322-96FA-3324CDBF1AA7"), 1
    ),
    "unknown_pellet_ccs_input91": AreaAnalyzeClass(
        uuid.UUID("75275C6E-E46A-44DD-A446-EEE872465909"), 1
    ),
    "unknown_pellet_ccs_input92": AreaAnalyzeClass(
        uuid.UUID("EBEC48A8-FAAA-4177-9EA5-FD205F1028F0"), 1
    ),
    "unknown_pellet_ccs_input93": AreaAnalyzeClass(
        uuid.UUID("D1043751-0AEC-4258-A432-D667157C6A2A"), 1
    ),
    "unknown_pellet_ccs_input94": AreaAnalyzeClass(
        uuid.UUID("722B6CDE-C8CE-417C-BC76-5E37BB38F45E"), 1
    ),
    "unknown_pellet_ccs_input95": AreaAnalyzeClass(
        uuid.UUID("142E0A4A-B63F-45F8-8AF6-BFF148EBEAAC"), 1
    ),
    "unknown_pellet_ccs_input96": AreaAnalyzeClass(
        uuid.UUID("1E61FC6D-5351-4820-B505-73EF688F2D9A"), 1
    ),
    "unknown_pellet_ccs_input97": AreaAnalyzeClass(
        uuid.UUID("6625C7B5-862D-417E-BDA5-CA063E52264D"), 1
    ),
    "unknown_pellet_ccs_input98": AreaAnalyzeClass(
        uuid.UUID("48A692D5-0F15-46EE-AF8A-B6EFE4F63E08"), 1
    ),
    "unknown_pellet_ccs_input99": AreaAnalyzeClass(
        uuid.UUID("1103429A-B62F-4382-A0A4-36087D97A712"), 1
    ),
    "unknown_pellet_ccs_std": AreaAnalyzeClass(
        uuid.UUID("093649C3-208A-4AE3-BF03-62E619BF432B"), 2
    ),
    "unknown_pellet_description_input1": AreaAnalyzeClass(
        uuid.UUID("C0C3332A-A212-499F-8541-623764B5807B"), 1
    ),
    "unknown_pellet_feo_input1": AreaAnalyzeClass(
        uuid.UUID("0CB72A5B-8455-45FB-8EF2-6218920C5A2B"), 1
    ),
    "unknown_pellet_moisture_input": AreaAnalyzeClass(
        uuid.UUID("5E0150F4-CF85-4E36-BBAC-62733C2F253B"), 1
    ),
    "unknown_pellet_porosity_dry": AreaAnalyzeClass(
        uuid.UUID("72E4899A-56B4-4932-9807-6202CF87DD9B"), 1
    ),
    "unknown_pellet_porosity_result": AreaAnalyzeClass(
        uuid.UUID("8694CF34-E729-4CA8-92C8-6242855B182B"), 2
    ),
    "unknown_pellet_porosity_saturated": AreaAnalyzeClass(
        uuid.UUID("AE24A83C-4C31-42E3-9A47-625F0BE61ECB"), 1
    ),
    "unknown_pellet_porosity_suspended": AreaAnalyzeClass(
        uuid.UUID("B893DBDC-C715-43A8-A262-625473EC51BB"), 1
    ),
    "unknown_pellet_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("5128B5FB-B876-4A99-9151-627B5BED92CB"), 1
    ),
    "unknown_pellet_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("24152E48-3ADA-4DB5-BA79-62AF3867CC7B"), 2
    ),
    "unknown_pellet_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("5961F48D-EC27-4132-8B0A-620D9BC2F86B"), 1
    ),
    "unknown_pellet_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("6F83D90A-6613-439F-ABAF-62CF01B60A9B"), 2
    ),
    "unknown_pellet_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("998C51BB-7CE6-455C-8314-62118D609EAB"), 1
    ),
    "unknown_pellet_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("7EA48BA3-BE72-4291-9082-62A355443FAB"), 2
    ),
    "unknown_pellet_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("7B2E1DDB-FFCF-4F19-9261-62C1AE08103B"), 1
    ),
    "unknown_pellet_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("B49A96D5-D131-43E0-9E7D-6214C486490B"), 2
    ),
    "unknown_pellet_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("85AE4E02-75BB-40D6-823E-62248B5BEACB"), 1
    ),
    "unknown_pellet_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("4B4436BB-003A-4836-9389-6212282DEF5B"), 2
    ),
    "unknown_pellet_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("2BBAC1F9-4BF7-43DD-8DAF-622BEC6BA8BB"), 1
    ),
    "unknown_pellet_sulfur_input": AreaAnalyzeClass(
        uuid.UUID("5B3954E5-BFC6-4498-8C99-62488327703B"), 1
    ),
    "unknown_pellet_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("137B0CEA-8C7E-4FCC-B986-620FC47C116B"), 1
    ),
    "unknown_pellet_tumble_r5w": AreaAnalyzeClass(
        uuid.UUID("41602DFA-890F-4993-974A-628CA3020E7B"), 2
    ),
    "unknown_pellet_tumble_r63w": AreaAnalyzeClass(
        uuid.UUID("21AFC759-775A-4F51-AAAF-6252E73C442B"), 2
    ),
    "unknown_pellet_tumble_remain5": AreaAnalyzeClass(
        uuid.UUID("A4D829AD-FF84-4C0B-B446-6288E4FEFB2B"), 1
    ),
    "unknown_pellet_tumble_remain63": AreaAnalyzeClass(
        uuid.UUID("DA1BEF43-C917-4018-86F2-62B0807AC07B"), 1
    ),
    "unknown_pellet_tumble_weight": AreaAnalyzeClass(
        uuid.UUID("7F41C2FE-268A-4BA3-A7A3-624CCD5A383B"), 1
    ),
    "unknown_pellet_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("951050B5-A053-4D4E-9846-62210903818B"), 1
    ),
    "unknown_pellet_xray_cao": AreaAnalyzeClass(
        uuid.UUID("ACA4D255-6D21-4C80-9EFD-62A8035B7CDB"), 1
    ),
    "unknown_pellet_xray_fe": AreaAnalyzeClass(
        uuid.UUID("316C2EDB-E877-47C3-A94E-625635502A2B"), 1
    ),
    "unknown_pellet_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("E0312025-72ED-49CE-A224-62D2BA39A5CB"), 1
    ),
    "unknown_pellet_xray_mno": AreaAnalyzeClass(
        uuid.UUID("A6A1A012-091C-4542-82C3-625BFBCD496B"), 1
    ),
    "unknown_pellet_xray_p": AreaAnalyzeClass(
        uuid.UUID("A260F830-F006-4332-B34B-6289687283DB"), 1
    ),
    "unknown_pellet_xray_result": AreaAnalyzeClass(
        uuid.UUID("4A1AFFF3-0C62-42B4-AD1C-62F9374E0B2B"), 2
    ),
    "unknown_pellet_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("3E875043-B330-4F1D-B958-62B90A31C39B"), 1
    ),
    "unknown_pellet_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("0B41B4D7-FE90-488A-9975-62E3573E648B"), 1
    ),
    "unknown_spongeiron_atomic_k2o": AreaAnalyzeClass(
        uuid.UUID("F147B200-FBDC-4A2C-A8AF-87311E41FA0F"), 1
    ),
    "unknown_spongeiron_atomic_na2o": AreaAnalyzeClass(
        uuid.UUID("BC0955CF-AAE1-4967-AF41-58EFB706B55A"), 1
    ),
    "unknown_spongeiron_carbon_input": AreaAnalyzeClass(
        uuid.UUID("C106C534-701F-4118-89B3-37F450A4F23F"), 1
    ),
    "unknown_spongeiron_ccs_100": AreaAnalyzeClass(
        uuid.UUID("D4E86FEB-CE1F-44E2-99DA-0838C3C1EB0C"), 2
    ),
    "unknown_spongeiron_ccs_150": AreaAnalyzeClass(
        uuid.UUID("B7BC4076-8EB6-4CD1-A9B0-429951173D8C"), 2
    ),
    "unknown_spongeiron_ccs_50": AreaAnalyzeClass(
        uuid.UUID("3A81E769-10E5-4E35-81FD-A906FFB47AE6"), 2
    ),
    "unknown_spongeiron_ccs_avg": AreaAnalyzeClass(
        uuid.UUID("865AD1AB-DF9A-4AE3-A50A-EA888AA7EB99"), 2
    ),
    "unknown_spongeiron_ccs_input1": AreaAnalyzeClass(
        uuid.UUID("27590B10-9038-413B-AEF7-02D6E2F53180"), 1
    ),
    "unknown_spongeiron_ccs_input10": AreaAnalyzeClass(
        uuid.UUID("11C573F8-795C-4E75-A5DE-AF409ABFA0CA"), 1
    ),
    "unknown_spongeiron_ccs_input100": AreaAnalyzeClass(
        uuid.UUID("72F1FAA5-2C72-48DE-90E1-77B80D3A3F30"), 1
    ),
    "unknown_spongeiron_ccs_input11": AreaAnalyzeClass(
        uuid.UUID("A287CB36-5E59-4B4F-868B-7CB04B771261"), 1
    ),
    "unknown_spongeiron_ccs_input12": AreaAnalyzeClass(
        uuid.UUID("D911BB75-0F7A-4E36-B1DD-13EFB990CCF3"), 1
    ),
    "unknown_spongeiron_ccs_input13": AreaAnalyzeClass(
        uuid.UUID("96A23E62-2041-4B47-9735-61F86A0C070F"), 1
    ),
    "unknown_spongeiron_ccs_input14": AreaAnalyzeClass(
        uuid.UUID("5FBD077A-1561-49AA-AEA0-A1200BE3B05B"), 1
    ),
    "unknown_spongeiron_ccs_input15": AreaAnalyzeClass(
        uuid.UUID("8CF9A861-F021-446D-8199-4D2575EFD79F"), 1
    ),
    "unknown_spongeiron_ccs_input16": AreaAnalyzeClass(
        uuid.UUID("E00A6440-1F97-4DCB-8049-CAF2C0750BE3"), 1
    ),
    "unknown_spongeiron_ccs_input17": AreaAnalyzeClass(
        uuid.UUID("67C32A5A-B0AA-4F62-A650-FF9811A4C139"), 1
    ),
    "unknown_spongeiron_ccs_input18": AreaAnalyzeClass(
        uuid.UUID("2DF4701C-462C-4E3F-9582-7C26E0F260DD"), 1
    ),
    "unknown_spongeiron_ccs_input19": AreaAnalyzeClass(
        uuid.UUID("17A8A791-3286-449F-89B3-506B087CABAC"), 1
    ),
    "unknown_spongeiron_ccs_input2": AreaAnalyzeClass(
        uuid.UUID("750ED5F0-F6A4-46B1-9032-AEEA585DE37F"), 1
    ),
    "unknown_spongeiron_ccs_input20": AreaAnalyzeClass(
        uuid.UUID("C5D9A179-D2D2-497C-B949-C6B57308D49D"), 1
    ),
    "unknown_spongeiron_ccs_input21": AreaAnalyzeClass(
        uuid.UUID("9349D49D-D086-4CC1-98FB-9E32935A0BB5"), 1
    ),
    "unknown_spongeiron_ccs_input22": AreaAnalyzeClass(
        uuid.UUID("6D14824A-0A21-414B-9130-3D4F641EEB01"), 1
    ),
    "unknown_spongeiron_ccs_input23": AreaAnalyzeClass(
        uuid.UUID("7769AA20-90BA-419B-9837-7C0385DA2BE5"), 1
    ),
    "unknown_spongeiron_ccs_input24": AreaAnalyzeClass(
        uuid.UUID("3D999B06-4FE5-48F0-B070-6D4897D3CA97"), 1
    ),
    "unknown_spongeiron_ccs_input25": AreaAnalyzeClass(
        uuid.UUID("64B53E14-880D-4E70-A63E-A4C0DAA77D30"), 1
    ),
    "unknown_spongeiron_ccs_input26": AreaAnalyzeClass(
        uuid.UUID("406AE028-46AC-4F0B-8A50-86B4AEAA02C7"), 1
    ),
    "unknown_spongeiron_ccs_input27": AreaAnalyzeClass(
        uuid.UUID("5B66BEC2-B3DD-487A-8A8F-5D19737F4650"), 1
    ),
    "unknown_spongeiron_ccs_input28": AreaAnalyzeClass(
        uuid.UUID("988EA6FC-602D-46FC-B3E3-5DE317D4F019"), 1
    ),
    "unknown_spongeiron_ccs_input29": AreaAnalyzeClass(
        uuid.UUID("DC441341-289A-4863-9DF8-5190CD9AAFDE"), 1
    ),
    "unknown_spongeiron_ccs_input3": AreaAnalyzeClass(
        uuid.UUID("8A883A57-517D-4F3E-8ACE-C717D95BD2D8"), 1
    ),
    "unknown_spongeiron_ccs_input30": AreaAnalyzeClass(
        uuid.UUID("98FD620E-49DF-4650-9A7F-1981A9CC3A79"), 1
    ),
    "unknown_spongeiron_ccs_input31": AreaAnalyzeClass(
        uuid.UUID("F9B3404C-0E01-4149-A7C7-2196128384B9"), 1
    ),
    "unknown_spongeiron_ccs_input32": AreaAnalyzeClass(
        uuid.UUID("04EE0369-C4A2-48EE-A5CF-8661F943582F"), 1
    ),
    "unknown_spongeiron_ccs_input33": AreaAnalyzeClass(
        uuid.UUID("0C3CBCDE-CD4F-4603-9362-B5790F606873"), 1
    ),
    "unknown_spongeiron_ccs_input34": AreaAnalyzeClass(
        uuid.UUID("1DEE4FD3-58DD-48C3-AF7D-B70BBA2C7A70"), 1
    ),
    "unknown_spongeiron_ccs_input35": AreaAnalyzeClass(
        uuid.UUID("AD619562-301B-4A00-807E-4604A1CD9601"), 1
    ),
    "unknown_spongeiron_ccs_input36": AreaAnalyzeClass(
        uuid.UUID("D0F0E576-4CD8-4F6E-93E8-316336D6801E"), 1
    ),
    "unknown_spongeiron_ccs_input37": AreaAnalyzeClass(
        uuid.UUID("9ED947DA-1D07-4140-BACF-3EABEEE4B921"), 1
    ),
    "unknown_spongeiron_ccs_input38": AreaAnalyzeClass(
        uuid.UUID("714EFD2E-396C-46DE-AD7F-D1E7DC163769"), 1
    ),
    "unknown_spongeiron_ccs_input39": AreaAnalyzeClass(
        uuid.UUID("2C4A6AEA-2343-4769-9D12-41626F0E903A"), 1
    ),
    "unknown_spongeiron_ccs_input4": AreaAnalyzeClass(
        uuid.UUID("4E4B67CC-F21C-446E-87D0-81F069A49615"), 1
    ),
    "unknown_spongeiron_ccs_input40": AreaAnalyzeClass(
        uuid.UUID("B2775B5F-2F4D-417B-A9B8-E0A77B015897"), 1
    ),
    "unknown_spongeiron_ccs_input41": AreaAnalyzeClass(
        uuid.UUID("65EDA9C6-F493-4D2A-AFE0-CC6FA427C321"), 1
    ),
    "unknown_spongeiron_ccs_input42": AreaAnalyzeClass(
        uuid.UUID("1CC7396F-8AEB-4146-B992-136B0F0EB90A"), 1
    ),
    "unknown_spongeiron_ccs_input43": AreaAnalyzeClass(
        uuid.UUID("072B616C-7B01-45D8-9362-E31A042E7EA5"), 1
    ),
    "unknown_spongeiron_ccs_input44": AreaAnalyzeClass(
        uuid.UUID("AC44FD86-A78E-4427-8A02-FA40AFC03CDB"), 1
    ),
    "unknown_spongeiron_ccs_input45": AreaAnalyzeClass(
        uuid.UUID("34B176A2-E187-4D1A-A388-FE06C0A13E6F"), 1
    ),
    "unknown_spongeiron_ccs_input46": AreaAnalyzeClass(
        uuid.UUID("24CAE3AE-7373-48B6-A5FB-4073EF939373"), 1
    ),
    "unknown_spongeiron_ccs_input47": AreaAnalyzeClass(
        uuid.UUID("743308DD-5CD9-4468-B961-6D688523A265"), 1
    ),
    "unknown_spongeiron_ccs_input48": AreaAnalyzeClass(
        uuid.UUID("042F355F-14B5-4163-996A-BC4CE549017B"), 1
    ),
    "unknown_spongeiron_ccs_input49": AreaAnalyzeClass(
        uuid.UUID("A8D6AC2B-6F85-4712-94A6-7460C7CF23A2"), 1
    ),
    "unknown_spongeiron_ccs_input5": AreaAnalyzeClass(
        uuid.UUID("0FA2D096-83F0-425C-8B99-E6BD4876B6E7"), 1
    ),
    "unknown_spongeiron_ccs_input50": AreaAnalyzeClass(
        uuid.UUID("81DCAC41-C384-421C-8882-75B27192A51C"), 1
    ),
    "unknown_spongeiron_ccs_input51": AreaAnalyzeClass(
        uuid.UUID("CDE14006-B6EE-485E-9421-F53309B3E5B0"), 1
    ),
    "unknown_spongeiron_ccs_input52": AreaAnalyzeClass(
        uuid.UUID("B49C6022-2632-49F8-B635-BA4C890C1D6A"), 1
    ),
    "unknown_spongeiron_ccs_input53": AreaAnalyzeClass(
        uuid.UUID("B5050A1E-A25B-47BF-A01C-BFA96905195B"), 1
    ),
    "unknown_spongeiron_ccs_input54": AreaAnalyzeClass(
        uuid.UUID("E667CEC0-9278-40DD-B2C5-308A6878455B"), 1
    ),
    "unknown_spongeiron_ccs_input55": AreaAnalyzeClass(
        uuid.UUID("01EB35DA-D122-4DD3-B563-EBB7B7BD2C1B"), 1
    ),
    "unknown_spongeiron_ccs_input56": AreaAnalyzeClass(
        uuid.UUID("3D28EEB1-9212-46CE-82A2-1951605A9A16"), 1
    ),
    "unknown_spongeiron_ccs_input57": AreaAnalyzeClass(
        uuid.UUID("B1440FC0-BF60-46AA-AC33-CB3915F1EB05"), 1
    ),
    "unknown_spongeiron_ccs_input58": AreaAnalyzeClass(
        uuid.UUID("9B697525-4582-4CC8-B4A9-3751BA2F9344"), 1
    ),
    "unknown_spongeiron_ccs_input59": AreaAnalyzeClass(
        uuid.UUID("BA26F8F0-E497-414E-9CBA-50C1E503478A"), 1
    ),
    "unknown_spongeiron_ccs_input6": AreaAnalyzeClass(
        uuid.UUID("22A57033-C67E-49F5-A364-28285C779946"), 1
    ),
    "unknown_spongeiron_ccs_input60": AreaAnalyzeClass(
        uuid.UUID("84B8590A-34E6-49DB-B23E-6EB43D41A4E6"), 1
    ),
    "unknown_spongeiron_ccs_input61": AreaAnalyzeClass(
        uuid.UUID("A314F6A6-CCBD-400F-A57D-7C7C53FD609F"), 1
    ),
    "unknown_spongeiron_ccs_input62": AreaAnalyzeClass(
        uuid.UUID("8950C07E-87DE-4C47-ABBE-6077361D9223"), 1
    ),
    "unknown_spongeiron_ccs_input63": AreaAnalyzeClass(
        uuid.UUID("C256960D-D1BE-474E-8234-BCAB63828858"), 1
    ),
    "unknown_spongeiron_ccs_input64": AreaAnalyzeClass(
        uuid.UUID("1E1D774F-B3DF-438C-9913-8E2B7D9AFA30"), 1
    ),
    "unknown_spongeiron_ccs_input65": AreaAnalyzeClass(
        uuid.UUID("FFEB227E-37ED-4F9B-8F9B-B1586E2EBE34"), 1
    ),
    "unknown_spongeiron_ccs_input66": AreaAnalyzeClass(
        uuid.UUID("725D3B86-752A-4B94-8441-7D1983EE8ACB"), 1
    ),
    "unknown_spongeiron_ccs_input67": AreaAnalyzeClass(
        uuid.UUID("244C6BDA-22E8-4391-AD9E-C9933F48457A"), 1
    ),
    "unknown_spongeiron_ccs_input68": AreaAnalyzeClass(
        uuid.UUID("171F9F73-7FA3-4C92-865C-53C72D7E882B"), 1
    ),
    "unknown_spongeiron_ccs_input69": AreaAnalyzeClass(
        uuid.UUID("98C3DFF0-C933-45F7-A68A-CCE8C6035875"), 1
    ),
    "unknown_spongeiron_ccs_input7": AreaAnalyzeClass(
        uuid.UUID("8E95D294-F7E6-4A13-AAC5-8477243916F2"), 1
    ),
    "unknown_spongeiron_ccs_input70": AreaAnalyzeClass(
        uuid.UUID("3527DCED-06E6-4033-BF46-8A8525676CE5"), 1
    ),
    "unknown_spongeiron_ccs_input71": AreaAnalyzeClass(
        uuid.UUID("6642EF81-3761-43A5-B135-4810BB60FDBF"), 1
    ),
    "unknown_spongeiron_ccs_input72": AreaAnalyzeClass(
        uuid.UUID("D4416E97-5E2A-4E80-AC59-88EC80AD1B4C"), 1
    ),
    "unknown_spongeiron_ccs_input73": AreaAnalyzeClass(
        uuid.UUID("20501896-28B3-44E6-9D96-C2DF393DD4B3"), 1
    ),
    "unknown_spongeiron_ccs_input74": AreaAnalyzeClass(
        uuid.UUID("40F08F99-6F75-4BB8-8231-A8D0112F301B"), 1
    ),
    "unknown_spongeiron_ccs_input75": AreaAnalyzeClass(
        uuid.UUID("A2C1CFA1-E26F-4858-95D4-7490C671C1EA"), 1
    ),
    "unknown_spongeiron_ccs_input76": AreaAnalyzeClass(
        uuid.UUID("C6B6734D-69FD-45AF-8212-8962ADF32C7E"), 1
    ),
    "unknown_spongeiron_ccs_input77": AreaAnalyzeClass(
        uuid.UUID("41333E58-EDB4-4D42-8A76-3FC1960D6BB8"), 1
    ),
    "unknown_spongeiron_ccs_input78": AreaAnalyzeClass(
        uuid.UUID("DCC4E945-A0E8-4B0B-A201-598EC032597C"), 1
    ),
    "unknown_spongeiron_ccs_input79": AreaAnalyzeClass(
        uuid.UUID("9552A2ED-B5E8-4DAC-B2F3-DE324C6EAB51"), 1
    ),
    "unknown_spongeiron_ccs_input8": AreaAnalyzeClass(
        uuid.UUID("0E3A85A5-DBAD-4644-8901-AD88D35F513E"), 1
    ),
    "unknown_spongeiron_ccs_input80": AreaAnalyzeClass(
        uuid.UUID("CB336DDD-C107-4C29-89B6-88178D017C14"), 1
    ),
    "unknown_spongeiron_ccs_input81": AreaAnalyzeClass(
        uuid.UUID("CEC5CAB1-916D-43A4-ACC0-F03733BE1158"), 1
    ),
    "unknown_spongeiron_ccs_input82": AreaAnalyzeClass(
        uuid.UUID("ADA283F8-2C16-41FE-9522-02A09BF52D47"), 1
    ),
    "unknown_spongeiron_ccs_input83": AreaAnalyzeClass(
        uuid.UUID("3BD747CC-2254-4F20-A6E5-E9F422DA616E"), 1
    ),
    "unknown_spongeiron_ccs_input84": AreaAnalyzeClass(
        uuid.UUID("27119995-A654-492A-A082-E0D8386138CA"), 1
    ),
    "unknown_spongeiron_ccs_input85": AreaAnalyzeClass(
        uuid.UUID("3A8FB027-4879-4A37-A92A-F3179822F4FD"), 1
    ),
    "unknown_spongeiron_ccs_input86": AreaAnalyzeClass(
        uuid.UUID("FDB69222-D1F9-4316-8DA0-3DB6945BEE82"), 1
    ),
    "unknown_spongeiron_ccs_input87": AreaAnalyzeClass(
        uuid.UUID("7211E904-CFC7-41B1-9A64-3AA48985FDF3"), 1
    ),
    "unknown_spongeiron_ccs_input88": AreaAnalyzeClass(
        uuid.UUID("E67502C9-5FCB-4949-90E2-7ED08C24EBD6"), 1
    ),
    "unknown_spongeiron_ccs_input89": AreaAnalyzeClass(
        uuid.UUID("EE0CBEDE-D89F-41A4-9BC1-77B1BBADA303"), 1
    ),
    "unknown_spongeiron_ccs_input9": AreaAnalyzeClass(
        uuid.UUID("0E72746F-83E2-446D-866E-05CC16722F04"), 1
    ),
    "unknown_spongeiron_ccs_input90": AreaAnalyzeClass(
        uuid.UUID("2CD8B4FB-DC0D-4F02-AB7A-128279F0BD44"), 1
    ),
    "unknown_spongeiron_ccs_input91": AreaAnalyzeClass(
        uuid.UUID("FBC4E0E3-E288-4FC0-8221-0C267626FBFA"), 1
    ),
    "unknown_spongeiron_ccs_input92": AreaAnalyzeClass(
        uuid.UUID("9B48B6D0-9FBB-48D2-8105-0896BDA535F7"), 1
    ),
    "unknown_spongeiron_ccs_input93": AreaAnalyzeClass(
        uuid.UUID("D2BB1664-AE07-4C19-A79A-A0593C7F24A8"), 1
    ),
    "unknown_spongeiron_ccs_input94": AreaAnalyzeClass(
        uuid.UUID("175EC404-C3A0-4122-B03B-A85E7C7002D3"), 1
    ),
    "unknown_spongeiron_ccs_input95": AreaAnalyzeClass(
        uuid.UUID("68E9B1ED-24FF-487D-A8A3-B3A6CAE48CE1"), 1
    ),
    "unknown_spongeiron_ccs_input96": AreaAnalyzeClass(
        uuid.UUID("5328C24F-D594-411C-8A65-A87928CE3FC1"), 1
    ),
    "unknown_spongeiron_ccs_input97": AreaAnalyzeClass(
        uuid.UUID("530ECA88-12E5-4228-A42E-73DFB3E0612C"), 1
    ),
    "unknown_spongeiron_ccs_input98": AreaAnalyzeClass(
        uuid.UUID("AC9A83DE-20C4-4A39-9248-751923E8DAEB"), 1
    ),
    "unknown_spongeiron_ccs_input99": AreaAnalyzeClass(
        uuid.UUID("B48DE760-C4E1-441D-975F-A903F7E4C298"), 1
    ),
    "unknown_spongeiron_ccs_std": AreaAnalyzeClass(
        uuid.UUID("3942E179-98A2-4702-B5E8-7499FCB1DC20"), 2
    ),
    "unknown_spongeiron_mfe_avg": AreaAnalyzeClass(
        uuid.UUID("3670B3C7-E27D-4031-80E3-C4132FE59260"), 1
    ),
    "unknown_spongeiron_mfe_input1": AreaAnalyzeClass(
        uuid.UUID("F91F342F-EDF1-4A95-B763-6D8198477D88"), 1
    ),
    "unknown_spongeiron_mfe_input2": AreaAnalyzeClass(
        uuid.UUID("5E3CE1BC-C5B7-40D3-92A3-46489A2514BD"), 1
    ),
    "unknown_spongeiron_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("A16BC927-CF47-4192-A796-D0EB11925F21"), 1
    ),
    "unknown_spongeiron_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("CEF5D375-22A1-45BE-97AC-52D6EA1E44E3"), 2
    ),
    "unknown_spongeiron_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("2BD887C4-4AE2-4113-BD5C-BC16705F66EE"), 1
    ),
    "unknown_spongeiron_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("B6A8156C-BC30-40EF-B46B-107DAC296CF7"), 2
    ),
    "unknown_spongeiron_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("6911ED1E-1776-492C-AE93-9267DBFB5DE5"), 1
    ),
    "unknown_spongeiron_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("8B0DD867-B009-4338-B954-867A707D65A5"), 2
    ),
    "unknown_spongeiron_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("8642ABFC-4F81-4F62-9FD2-51A2FC5923EC"), 1
    ),
    "unknown_spongeiron_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("2164ED8A-EEEA-411E-88F6-EBB4518EFE52"), 2
    ),
    "unknown_spongeiron_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("F0AFCB15-DC6D-44FA-BB55-5B3F02A0C636"), 1
    ),
    "unknown_spongeiron_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("2D8AC004-3C57-4FDB-B77E-26BB916D7586"), 2
    ),
    "unknown_spongeiron_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("36CBB5A3-B837-4815-A8AB-512A50DF03E9"), 1
    ),
    "unknown_spongeiron_sulfur_input": AreaAnalyzeClass(
        uuid.UUID("F945D3C5-578F-4274-A713-97EFA502C63E"), 1
    ),
    "unknown_spongeiron_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("0E6F309A-C02D-403E-BB2D-929E006C1A84"), 2
    ),
    "unknown_spongeiron_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("0DA64362-587F-4C8C-AC4D-B50D63BB865D"), 1
    ),
    "unknown_spongeiron_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("1F37D25F-4952-4BE4-B5AE-EFD94AFAAB7C"), 1
    ),
    "unknown_spongeiron_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("D18D678A-30A2-41F6-9145-4785EE3F2FA5"), 1
    ),
    "unknown_spongeiron_xray_cao": AreaAnalyzeClass(
        uuid.UUID("AE7F1AAB-EBB5-4354-A847-C11DDDD271E3"), 1
    ),
    "unknown_spongeiron_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("08EAA040-72E8-4146-AA90-B2F39F4ED160"), 1
    ),
    "unknown_spongeiron_xray_mno": AreaAnalyzeClass(
        uuid.UUID("EE2EE6EE-A6D0-4A25-9C21-39D7EC214B0A"), 1
    ),
    "unknown_spongeiron_xray_p": AreaAnalyzeClass(
        uuid.UUID("6F85BD11-1CDA-457A-883A-99AA35C4B082"), 1
    ),
    "unknown_spongeiron_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("E7273B07-64B8-496F-A6CB-0CD8D003B046"), 1
    ),
    "unknown_spongeiron_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("ED99B3E6-E94B-42CE-9AF2-BBBB0902B776"), 1
    ),
    "unusual_bentonite_45micron_passing": AreaAnalyzeClass(
        uuid.UUID("12669BCC-61CA-4B5F-B8DA-85334CAA5ABA"), 2
    ),
    "unusual_bentonite_45micron_wa": AreaAnalyzeClass(
        uuid.UUID("00329313-212B-44B7-A36B-BEA4DE073819"), 1
    ),
    "unusual_bentonite_45micron_wb": AreaAnalyzeClass(
        uuid.UUID("C3278319-7D4F-4F59-9777-9E5636CB1A91"), 1
    ),
    "unusual_bentonite_45micron_ws": AreaAnalyzeClass(
        uuid.UUID("7A7E90F3-27AA-4983-9901-7E958B12AB56"), 1
    ),
    "unusual_bentonite_loi_input": AreaAnalyzeClass(
        uuid.UUID("3C725C9F-6203-43B0-83AC-5597719208BE"), 2
    ),
    "unusual_bentonite_moisture_input": AreaAnalyzeClass(
        uuid.UUID("FFCBDA7E-1D19-451A-9B03-72CCD6E2D9BC"), 1
    ),
    "unusual_bentonite_waterabsorption_k": AreaAnalyzeClass(
        uuid.UUID("9F36FAA5-590C-4F55-9169-7D3F444A749B"), 1
    ),
    "unusual_bentonite_waterabsorption_result": AreaAnalyzeClass(
        uuid.UUID("7E9BDDD7-4795-46DB-AC19-DF4920B6A455"), 1
    ),
    "unusual_bentonite_waterabsorption_t1": AreaAnalyzeClass(
        uuid.UUID("2518749C-4806-4EAF-A812-A606AD4F8DD4"), 1
    ),
    "unusual_bentonite_waterabsorption_t2": AreaAnalyzeClass(
        uuid.UUID("E544ACDD-21C8-446C-81CD-34306A232495"), 1
    ),
    "unusual_bentonite_waterabsorption_tr": AreaAnalyzeClass(
        uuid.UUID("498EE26C-D5E2-46E3-8369-7B7E5F860E12"), 1
    ),
    "unusual_bentonite_waterabsorption_w0": AreaAnalyzeClass(
        uuid.UUID("C9B8715C-F199-47A6-B0E8-C3DB2C46614E"), 1
    ),
    "unusual_bentonite_waterabsorption_w1": AreaAnalyzeClass(
        uuid.UUID("F78E6864-F9FC-4879-8FE8-A3D9F84EBA55"), 1
    ),
    "unusual_bentonite_waterabsorption_w2": AreaAnalyzeClass(
        uuid.UUID("70B343A9-97F4-4701-A684-5DE79706BABE"), 1
    ),
    "unusual_bentonite_waterabsorption2_k": AreaAnalyzeClass(
        uuid.UUID("D2842DD9-7001-4E13-B5C3-65380C6B3578"), 1
    ),
    "unusual_bentonite_waterabsorption2_result": AreaAnalyzeClass(
        uuid.UUID("B8BF1407-B0C9-424B-9744-AC56429ECF26"), 2
    ),
    "unusual_bentonite_waterabsorption2_t1": AreaAnalyzeClass(
        uuid.UUID("C7131026-28AC-4A39-B08B-60BA8C792DF9"), 1
    ),
    "unusual_bentonite_waterabsorption2_t2": AreaAnalyzeClass(
        uuid.UUID("2EFA22C5-A460-43C5-9A30-0614B908EE79"), 1
    ),
    "unusual_bentonite_waterabsorption2_tr": AreaAnalyzeClass(
        uuid.UUID("2873E0BF-ECAA-4046-B602-F363F3CCB535"), 1
    ),
    "unusual_bentonite_waterabsorption2_w0": AreaAnalyzeClass(
        uuid.UUID("62DD9E6B-A2FD-4B55-A0B0-BAF7132FC372"), 1
    ),
    "unusual_bentonite_waterabsorption2_w1": AreaAnalyzeClass(
        uuid.UUID("1303AC52-6D03-42D7-B7EF-2F839480C64D"), 1
    ),
    "unusual_bentonite_waterabsorption2_w2": AreaAnalyzeClass(
        uuid.UUID("5A58B731-846A-43D6-8EA1-E075901E9379"), 1
    ),
    "unusual_bentonite_waterabsorption3_k": AreaAnalyzeClass(
        uuid.UUID("37EBD6CA-FBB6-43A2-BD1A-F1F19050BD92"), 1
    ),
    "unusual_bentonite_waterabsorption3_result": AreaAnalyzeClass(
        uuid.UUID("C594E775-0D16-4689-92C6-A5CF6FEC9BBE"), 2
    ),
    "unusual_bentonite_waterabsorption3_t1": AreaAnalyzeClass(
        uuid.UUID("7FBF1B5B-23C4-4983-AEB0-EC17CB1F79CB"), 1
    ),
    "unusual_bentonite_waterabsorption3_t2": AreaAnalyzeClass(
        uuid.UUID("E9B34BE8-29B9-4FC1-852F-49854711B0F7"), 1
    ),
    "unusual_bentonite_waterabsorption3_tr": AreaAnalyzeClass(
        uuid.UUID("2CA99B50-FFA1-45B0-BA52-5106ED44C536"), 1
    ),
    "unusual_bentonite_waterabsorption3_w0": AreaAnalyzeClass(
        uuid.UUID("485CB920-F47A-4E25-98CB-6E8A94E27587"), 1
    ),
    "unusual_bentonite_waterabsorption3_w1": AreaAnalyzeClass(
        uuid.UUID("C7619830-353A-40AB-A966-82F06EF20889"), 1
    ),
    "unusual_bentonite_waterabsorption3_w2": AreaAnalyzeClass(
        uuid.UUID("2C49AC27-9851-4391-9D5C-9BBD390A6AD7"), 1
    ),
    "unusual_bentonite_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("A256E71C-F49F-445C-9EF5-9EC1060D3F33"), 1
    ),
    "unusual_bentonite_xray_cao": AreaAnalyzeClass(
        uuid.UUID("B2B7E80A-FA24-43E0-85FB-E8BA549731C3"), 1
    ),
    "unusual_bentonite_xray_fe": AreaAnalyzeClass(
        uuid.UUID("418BC707-0B48-4EFD-9220-97384F0DF65A"), 1
    ),
    "unusual_bentonite_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("CD6FF70E-C2E9-4C11-8A8B-3E568C01600B"), 1
    ),
    "unusual_bentonite_xray_mno": AreaAnalyzeClass(
        uuid.UUID("84ED0DFB-7EB6-45CA-BD51-11A4BC5A8428"), 1
    ),
    "unusual_bentonite_xray_p": AreaAnalyzeClass(
        uuid.UUID("6E0304D7-6D0C-4F4A-AC55-F53964364689"), 1
    ),
    "unusual_bentonite_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("9431F59B-4866-40F1-AB64-3D57B6071F30"), 1
    ),
    "unusual_bentonite_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("2DB3A137-566B-46D4-8D60-BF6F27F9F7B0"), 1
    ),
    "unusual_concentrate_20micron_passing": AreaAnalyzeClass(
        uuid.UUID("FA097EA4-3D99-4626-BD0D-046470ABF7D6"), 2
    ),
    "unusual_concentrate_20micron_wa": AreaAnalyzeClass(
        uuid.UUID("60DB82C0-9423-43FC-8575-29DBCED88C74"), 1
    ),
    "unusual_concentrate_20micron_wb": AreaAnalyzeClass(
        uuid.UUID("286C5265-F35D-45CC-8C9A-87B7E17D70C9"), 1
    ),
    "unusual_concentrate_20micron_ws": AreaAnalyzeClass(
        uuid.UUID("770DA4E0-0E18-4198-A8EE-63883F7AFEB7"), 1
    ),
    "unusual_concentrate_25micron_passing": AreaAnalyzeClass(
        uuid.UUID("CDBE8271-BD62-4CA4-ABA1-F78620A952DE"), 2
    ),
    "unusual_concentrate_25micron_wa": AreaAnalyzeClass(
        uuid.UUID("E2E97010-44CF-4A82-94D4-FD5603B0186A"), 1
    ),
    "unusual_concentrate_25micron_wb": AreaAnalyzeClass(
        uuid.UUID("9A48941A-7649-4948-AE10-008E6C2867CF"), 1
    ),
    "unusual_concentrate_25micron_ws": AreaAnalyzeClass(
        uuid.UUID("495BECA3-151F-4045-A1F4-29133F941CE7"), 1
    ),
    "unusual_concentrate_45micron_passing": AreaAnalyzeClass(
        uuid.UUID("269C63D0-691D-47E0-A5B6-2ADFF5951214"), 2
    ),
    "unusual_concentrate_45micron_wa": AreaAnalyzeClass(
        uuid.UUID("3A5D9CC7-34FB-48D6-96F1-72397F4A411F"), 1
    ),
    "unusual_concentrate_45micron_wb": AreaAnalyzeClass(
        uuid.UUID("2ED42754-B2BF-4AE6-9FF7-29BA77499DC7"), 1
    ),
    "unusual_concentrate_45micron_ws": AreaAnalyzeClass(
        uuid.UUID("A2587768-D073-481C-9DE9-A36445955649"), 1
    ),
    "unusual_concentrate_atomic_k2o": AreaAnalyzeClass(
        uuid.UUID("B74CB73F-388D-42FA-8343-A309DA74C27B"), 1
    ),
    "unusual_concentrate_atomic_na2o": AreaAnalyzeClass(
        uuid.UUID("4279BB97-23CE-4412-8EEC-FCE99C2174B7"), 1
    ),
    "unusual_concentrate_blaine_b": AreaAnalyzeClass(
        uuid.UUID("7ACF11E4-9A93-4385-8890-6C5A75624894"), 1
    ),
    "unusual_concentrate_blaine_bs": AreaAnalyzeClass(
        uuid.UUID("0DBFABE8-95A6-46B6-864E-FDC819B13E3B"), 1
    ),
    "unusual_concentrate_blaine_e": AreaAnalyzeClass(
        uuid.UUID("FDDB3226-E841-48F5-9D40-FD1AF6EE4189"), 1
    ),
    "unusual_concentrate_blaine_es": AreaAnalyzeClass(
        uuid.UUID("4E638C54-3235-4D86-A937-F28FE901A827"), 1
    ),
    "unusual_concentrate_blaine_p": AreaAnalyzeClass(
        uuid.UUID("0F265B7A-EE5C-48FD-AB69-5290EE82BA45"), 1
    ),
    "unusual_concentrate_blaine_ps": AreaAnalyzeClass(
        uuid.UUID("7AA3D8A9-A0DF-4E54-AEC1-9C21749CF0DB"), 1
    ),
    "unusual_concentrate_blaine_result": AreaAnalyzeClass(
        uuid.UUID("9DFCAAA1-D36D-4E09-AA95-605FE57EA400"), 2
    ),
    "unusual_concentrate_blaine_ss": AreaAnalyzeClass(
        uuid.UUID("D2D06E42-39EC-4D14-A7CC-CE48F1DBBBA2"), 1
    ),
    "unusual_concentrate_blaine_t": AreaAnalyzeClass(
        uuid.UUID("D440755E-9644-4D96-9134-BDDDCCE81A04"), 1
    ),
    "unusual_concentrate_blaine_ts": AreaAnalyzeClass(
        uuid.UUID("B215DC0C-5896-49A9-A039-E332D3D5F553"), 1
    ),
    "unusual_concentrate_feo_avg": AreaAnalyzeClass(
        uuid.UUID("8A1ECB41-B0C2-4AE8-A153-311A31A8BB5E"), 2
    ),
    "unusual_concentrate_feo_input1": AreaAnalyzeClass(
        uuid.UUID("918BC619-DDEB-45D3-B79C-1D2508773224"), 1
    ),
    "unusual_concentrate_feo_input2": AreaAnalyzeClass(
        uuid.UUID("DE60DD3F-6AAA-4C5B-B7F3-EA602ECF0942"), 1
    ),
    "unusual_concentrate_moisture_input": AreaAnalyzeClass(
        uuid.UUID("32DC796C-03A2-42F4-9BBB-7DE758BC419C"), 1
    ),
    "unusual_concentrate_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("C4BF3C7E-1132-43C8-BE4E-CAFA154BF38C"), 2
    ),
    "unusual_concentrate_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("61D60E72-3CF7-4B62-8D2B-2251D6CE5ABF"), 1
    ),
    "unusual_concentrate_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("4B7E5385-F893-4B16-AE1E-BBDCFD4B4976"), 1
    ),
    "unusual_concentrate_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("C74C6776-649A-4F5C-B518-E16800CF992E"), 1
    ),
    "unusual_concentrate_xray_cao": AreaAnalyzeClass(
        uuid.UUID("1816ADA8-A63F-4ADF-8776-304BB140B20E"), 1
    ),
    "unusual_concentrate_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("1209CDA5-3409-4700-A9C9-DF4C5FE4E5FE"), 1
    ),
    "unusual_concentrate_xray_mno": AreaAnalyzeClass(
        uuid.UUID("330E6F22-9D85-4C06-8DEC-E8F18C23F4CF"), 1
    ),
    "unusual_concentrate_xray_p": AreaAnalyzeClass(
        uuid.UUID("2FA27748-9758-4303-A485-7884C18696E2"), 1
    ),
    "unusual_concentrate_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("F15D8759-8F43-4C72-930D-3FF6C5E29C18"), 1
    ),
    "unusual_concentrate_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("41058783-408E-435F-A6D1-18434BF21D76"), 1
    ),
    "unusual_pellet_ccs_100": AreaAnalyzeClass(
        uuid.UUID("C9F5F155-44A5-40B9-AF04-567579D6B3E8"), 2
    ),
    "unusual_pellet_ccs_150": AreaAnalyzeClass(
        uuid.UUID("6D4AE8F5-623E-4492-831A-D299CFCCF699"), 2
    ),
    "unusual_pellet_ccs_50": AreaAnalyzeClass(
        uuid.UUID("E13B21BE-FCB5-494C-A812-1BBF13B5935C"), 2
    ),
    "unusual_pellet_ccs_avg": AreaAnalyzeClass(
        uuid.UUID("AD6A216A-25F3-49F4-AE30-B846C55E3F14"), 2
    ),
    "unusual_pellet_ccs_input1": AreaAnalyzeClass(
        uuid.UUID("F4BA21B8-770C-45AD-93B7-67DE6516B893"), 1
    ),
    "unusual_pellet_ccs_input10": AreaAnalyzeClass(
        uuid.UUID("4FA325FC-F27E-483E-9AB5-9CA82EBFC1E6"), 1
    ),
    "unusual_pellet_ccs_input100": AreaAnalyzeClass(
        uuid.UUID("33F20BA3-4233-4E2D-9973-AE05FAEDC60B"), 1
    ),
    "unusual_pellet_ccs_input11": AreaAnalyzeClass(
        uuid.UUID("990F9750-50C7-408C-8F51-35BD6D33D1A0"), 1
    ),
    "unusual_pellet_ccs_input12": AreaAnalyzeClass(
        uuid.UUID("2F0F0C18-0D3E-4588-A9E7-24E2F26AD672"), 1
    ),
    "unusual_pellet_ccs_input13": AreaAnalyzeClass(
        uuid.UUID("39F5F415-19F9-4232-B288-67ED7DCB422C"), 1
    ),
    "unusual_pellet_ccs_input14": AreaAnalyzeClass(
        uuid.UUID("481C6D68-F051-4280-BB9E-B81D5D286744"), 1
    ),
    "unusual_pellet_ccs_input15": AreaAnalyzeClass(
        uuid.UUID("384FDDF0-0EFD-4818-8978-62D7CDF7BAC0"), 1
    ),
    "unusual_pellet_ccs_input16": AreaAnalyzeClass(
        uuid.UUID("C32B712D-4EE0-40E8-B8F0-2451C548FCFB"), 1
    ),
    "unusual_pellet_ccs_input17": AreaAnalyzeClass(
        uuid.UUID("B4AA42DB-4413-46A4-BF02-8380FD9E4086"), 1
    ),
    "unusual_pellet_ccs_input18": AreaAnalyzeClass(
        uuid.UUID("6CF0BA65-422C-4E1B-868D-54EC6FA9596F"), 1
    ),
    "unusual_pellet_ccs_input19": AreaAnalyzeClass(
        uuid.UUID("734403DE-AFCA-44C1-B116-FECBB03ED375"), 1
    ),
    "unusual_pellet_ccs_input2": AreaAnalyzeClass(
        uuid.UUID("19BA7F65-C93C-43BA-8184-13609E687957"), 1
    ),
    "unusual_pellet_ccs_input20": AreaAnalyzeClass(
        uuid.UUID("9656027E-7E9B-47D3-8FB8-6F32650266EC"), 1
    ),
    "unusual_pellet_ccs_input21": AreaAnalyzeClass(
        uuid.UUID("2C871D27-404F-404F-A611-AF642F93A043"), 1
    ),
    "unusual_pellet_ccs_input22": AreaAnalyzeClass(
        uuid.UUID("B4F572E9-68DB-4BD8-B891-E605896B3415"), 1
    ),
    "unusual_pellet_ccs_input23": AreaAnalyzeClass(
        uuid.UUID("6637AF08-A15A-4896-8E53-A70E5864A858"), 1
    ),
    "unusual_pellet_ccs_input24": AreaAnalyzeClass(
        uuid.UUID("479E3247-4FC3-497F-9418-D3842F8C8AF4"), 1
    ),
    "unusual_pellet_ccs_input25": AreaAnalyzeClass(
        uuid.UUID("E15DF333-9F2E-4137-B8BA-2BA1F2F3BFFD"), 1
    ),
    "unusual_pellet_ccs_input26": AreaAnalyzeClass(
        uuid.UUID("CC5836BD-165C-416E-B221-A1147AD486F9"), 1
    ),
    "unusual_pellet_ccs_input27": AreaAnalyzeClass(
        uuid.UUID("8C5C8334-F173-4049-BFFA-09FA6AB0C604"), 1
    ),
    "unusual_pellet_ccs_input28": AreaAnalyzeClass(
        uuid.UUID("AB2891CA-0B22-48A9-80B7-76167C85FAB7"), 1
    ),
    "unusual_pellet_ccs_input29": AreaAnalyzeClass(
        uuid.UUID("FB593037-068F-4827-BF15-A0EA91E4BA3B"), 1
    ),
    "unusual_pellet_ccs_input3": AreaAnalyzeClass(
        uuid.UUID("43190EA4-7795-43E3-AB40-0F269ABCE09C"), 1
    ),
    "unusual_pellet_ccs_input30": AreaAnalyzeClass(
        uuid.UUID("AFF1012D-A6C8-4880-B1C6-CA083DEB4AC9"), 1
    ),
    "unusual_pellet_ccs_input31": AreaAnalyzeClass(
        uuid.UUID("23F3177C-7A9C-4D87-BF83-0E7A2953826B"), 1
    ),
    "unusual_pellet_ccs_input32": AreaAnalyzeClass(
        uuid.UUID("472808CA-93E1-4E9E-8D20-D4FAD6BDB3DA"), 1
    ),
    "unusual_pellet_ccs_input33": AreaAnalyzeClass(
        uuid.UUID("F32B8875-228B-41A2-B9E4-94AFCD533F51"), 1
    ),
    "unusual_pellet_ccs_input34": AreaAnalyzeClass(
        uuid.UUID("2BFF48B5-21D9-44BF-BB45-2CEDA20B5D4B"), 1
    ),
    "unusual_pellet_ccs_input35": AreaAnalyzeClass(
        uuid.UUID("FCF83ADD-CD97-46BE-AF64-B5BDF55D04FC"), 1
    ),
    "unusual_pellet_ccs_input36": AreaAnalyzeClass(
        uuid.UUID("FCAF3046-0EFB-4795-8AC9-9B5117BF7484"), 1
    ),
    "unusual_pellet_ccs_input37": AreaAnalyzeClass(
        uuid.UUID("4AEE9131-9532-4283-81A0-10D7D629E9C6"), 1
    ),
    "unusual_pellet_ccs_input38": AreaAnalyzeClass(
        uuid.UUID("34134825-3E78-4660-8FCA-CBF3DCB67B1A"), 1
    ),
    "unusual_pellet_ccs_input39": AreaAnalyzeClass(
        uuid.UUID("B7C852F3-62A8-432D-BE72-2C47D90201C3"), 1
    ),
    "unusual_pellet_ccs_input4": AreaAnalyzeClass(
        uuid.UUID("66158810-6CFC-4AD8-AFAF-253EE7AF68FC"), 1
    ),
    "unusual_pellet_ccs_input40": AreaAnalyzeClass(
        uuid.UUID("00D737B8-382F-4D39-B1A9-A89A807630AF"), 1
    ),
    "unusual_pellet_ccs_input41": AreaAnalyzeClass(
        uuid.UUID("1E265AD4-A820-48BC-9EFF-448507997A19"), 1
    ),
    "unusual_pellet_ccs_input42": AreaAnalyzeClass(
        uuid.UUID("36FAB3F1-82B6-4197-9AF0-9B321C72D20C"), 1
    ),
    "unusual_pellet_ccs_input43": AreaAnalyzeClass(
        uuid.UUID("296DC573-9E60-423E-85FC-9914D166EB93"), 1
    ),
    "unusual_pellet_ccs_input44": AreaAnalyzeClass(
        uuid.UUID("178071BA-A08D-45FC-AEE0-CA2B1030B5AC"), 1
    ),
    "unusual_pellet_ccs_input45": AreaAnalyzeClass(
        uuid.UUID("A498BC05-D406-4256-86FA-43E60DF8D316"), 1
    ),
    "unusual_pellet_ccs_input46": AreaAnalyzeClass(
        uuid.UUID("58904EF8-88A3-45A8-8E9F-FA10DE099FF9"), 1
    ),
    "unusual_pellet_ccs_input47": AreaAnalyzeClass(
        uuid.UUID("C5E6A47F-C219-4C9E-82B7-A3761D637FFE"), 1
    ),
    "unusual_pellet_ccs_input48": AreaAnalyzeClass(
        uuid.UUID("20C38AE9-4CFB-4D4F-9AB4-CEC29A5D1C4A"), 1
    ),
    "unusual_pellet_ccs_input49": AreaAnalyzeClass(
        uuid.UUID("A54E19F9-C055-41C9-B426-3B18329E532D"), 1
    ),
    "unusual_pellet_ccs_input5": AreaAnalyzeClass(
        uuid.UUID("E9AA11C3-99BF-47DE-A357-AE44C7E87C5F"), 1
    ),
    "unusual_pellet_ccs_input50": AreaAnalyzeClass(
        uuid.UUID("4DE6BDED-0B0F-4FB1-A93B-DA307A66C288"), 1
    ),
    "unusual_pellet_ccs_input51": AreaAnalyzeClass(
        uuid.UUID("458A81A5-D1AE-42FB-A4F3-C0C7BB342234"), 1
    ),
    "unusual_pellet_ccs_input52": AreaAnalyzeClass(
        uuid.UUID("4BE4116B-E3F2-4D53-BC1D-50426F4A15A2"), 1
    ),
    "unusual_pellet_ccs_input53": AreaAnalyzeClass(
        uuid.UUID("B087CE28-E2D0-46F3-973D-0662CD0DEEEC"), 1
    ),
    "unusual_pellet_ccs_input54": AreaAnalyzeClass(
        uuid.UUID("5ECDD972-AB1C-4BF5-8CB1-46C63044D9AC"), 1
    ),
    "unusual_pellet_ccs_input55": AreaAnalyzeClass(
        uuid.UUID("A73D8684-B765-413E-97C6-A503B71A3D5A"), 1
    ),
    "unusual_pellet_ccs_input56": AreaAnalyzeClass(
        uuid.UUID("63B7FD99-BDD9-4050-9C74-8F12794FA702"), 1
    ),
    "unusual_pellet_ccs_input57": AreaAnalyzeClass(
        uuid.UUID("85FC5E21-E911-4B29-BB01-DADB94F28475"), 1
    ),
    "unusual_pellet_ccs_input58": AreaAnalyzeClass(
        uuid.UUID("CA66670C-F619-4C05-BF01-FCF7259A8BD6"), 1
    ),
    "unusual_pellet_ccs_input59": AreaAnalyzeClass(
        uuid.UUID("4A1322D1-D6F8-4321-A0A4-409FE75CCA5F"), 1
    ),
    "unusual_pellet_ccs_input6": AreaAnalyzeClass(
        uuid.UUID("6FE41919-5316-44C9-B6F4-404D434BD490"), 1
    ),
    "unusual_pellet_ccs_input60": AreaAnalyzeClass(
        uuid.UUID("9913A0F0-3C14-4094-9DBA-8A13293D9880"), 1
    ),
    "unusual_pellet_ccs_input61": AreaAnalyzeClass(
        uuid.UUID("05A3368C-E4E8-4254-ABD8-C513571D2896"), 1
    ),
    "unusual_pellet_ccs_input62": AreaAnalyzeClass(
        uuid.UUID("99398D2C-0A25-4556-8050-72DD70C17999"), 1
    ),
    "unusual_pellet_ccs_input63": AreaAnalyzeClass(
        uuid.UUID("E4A55065-EB40-4A36-8E1C-F1C8A92DC488"), 1
    ),
    "unusual_pellet_ccs_input64": AreaAnalyzeClass(
        uuid.UUID("A23D0769-843C-406F-8571-A16240FACD64"), 1
    ),
    "unusual_pellet_ccs_input65": AreaAnalyzeClass(
        uuid.UUID("2D2BA594-A3D3-4DA7-8135-6FFC6D688E8C"), 1
    ),
    "unusual_pellet_ccs_input66": AreaAnalyzeClass(
        uuid.UUID("B4711CC4-9ACA-41A3-A8DD-EADE58FEA9F0"), 1
    ),
    "unusual_pellet_ccs_input67": AreaAnalyzeClass(
        uuid.UUID("CE03BB4B-CC7D-4D19-B49E-78D3A80B6A65"), 1
    ),
    "unusual_pellet_ccs_input68": AreaAnalyzeClass(
        uuid.UUID("BB40ED5C-AB8E-4CF9-BCF0-365BBFACBC6B"), 1
    ),
    "unusual_pellet_ccs_input69": AreaAnalyzeClass(
        uuid.UUID("AB3AD41F-22B8-4B51-B262-04548B5E72C9"), 1
    ),
    "unusual_pellet_ccs_input7": AreaAnalyzeClass(
        uuid.UUID("AD03D9F4-9AE7-4CFF-9FD2-9DA24560DAA5"), 1
    ),
    "unusual_pellet_ccs_input70": AreaAnalyzeClass(
        uuid.UUID("333A0093-FC9B-44C9-9BF7-5E08C7BE14BC"), 1
    ),
    "unusual_pellet_ccs_input71": AreaAnalyzeClass(
        uuid.UUID("CFCD9F1C-4B10-417C-B21E-B94B2F4F7D6C"), 1
    ),
    "unusual_pellet_ccs_input72": AreaAnalyzeClass(
        uuid.UUID("E4BEBBE9-8A4D-4297-AF49-9F9D2CD2D614"), 1
    ),
    "unusual_pellet_ccs_input73": AreaAnalyzeClass(
        uuid.UUID("0E2A5C94-CF00-4709-B96A-B5F1A38E9BEA"), 1
    ),
    "unusual_pellet_ccs_input74": AreaAnalyzeClass(
        uuid.UUID("DF8CA1EA-8BCF-4362-8A40-428908EF5AE9"), 1
    ),
    "unusual_pellet_ccs_input75": AreaAnalyzeClass(
        uuid.UUID("7D4FA784-0D3B-4AFD-94AA-65DCAE740E3F"), 1
    ),
    "unusual_pellet_ccs_input76": AreaAnalyzeClass(
        uuid.UUID("2A21B0FD-CC6D-41E7-9B0A-EC33EF4DBF34"), 1
    ),
    "unusual_pellet_ccs_input77": AreaAnalyzeClass(
        uuid.UUID("9E83FAD5-CEA4-47FE-965B-175FA750DA19"), 1
    ),
    "unusual_pellet_ccs_input78": AreaAnalyzeClass(
        uuid.UUID("8C9BF4AA-2D17-4EAF-80D1-4E6F8B1AB290"), 1
    ),
    "unusual_pellet_ccs_input79": AreaAnalyzeClass(
        uuid.UUID("EAE9BEFD-B501-44AE-AA93-85F4EFDE8738"), 1
    ),
    "unusual_pellet_ccs_input8": AreaAnalyzeClass(
        uuid.UUID("1470ECC4-8FC0-4A3E-B7CF-F4D125C4B501"), 1
    ),
    "unusual_pellet_ccs_input80": AreaAnalyzeClass(
        uuid.UUID("F8DF3F43-60BE-438B-A35A-5BBB0B09B234"), 1
    ),
    "unusual_pellet_ccs_input81": AreaAnalyzeClass(
        uuid.UUID("EC68E167-A2FE-47E5-A377-AA3C1CA85AEA"), 1
    ),
    "unusual_pellet_ccs_input82": AreaAnalyzeClass(
        uuid.UUID("B3DA8253-74A4-49FC-AFE3-DE9435131F09"), 1
    ),
    "unusual_pellet_ccs_input83": AreaAnalyzeClass(
        uuid.UUID("F09A9682-95B5-418C-AF3E-1638EB77805A"), 1
    ),
    "unusual_pellet_ccs_input84": AreaAnalyzeClass(
        uuid.UUID("0046D238-A0CA-49A7-9967-7B17B7F36D39"), 1
    ),
    "unusual_pellet_ccs_input85": AreaAnalyzeClass(
        uuid.UUID("270F8B14-80CA-424B-A8CF-C16537EA3B57"), 1
    ),
    "unusual_pellet_ccs_input86": AreaAnalyzeClass(
        uuid.UUID("F6187828-215F-4F71-9130-74A111894CF4"), 1
    ),
    "unusual_pellet_ccs_input87": AreaAnalyzeClass(
        uuid.UUID("58A0844A-CA65-4FFB-9B10-E026E1B8D348"), 1
    ),
    "unusual_pellet_ccs_input88": AreaAnalyzeClass(
        uuid.UUID("BC2EA8A7-B7E2-41A4-A927-C4FCEAA58070"), 1
    ),
    "unusual_pellet_ccs_input89": AreaAnalyzeClass(
        uuid.UUID("E3F54DCB-46D9-4D5B-9D4B-FAFFC1FE8146"), 1
    ),
    "unusual_pellet_ccs_input9": AreaAnalyzeClass(
        uuid.UUID("77A79296-0905-42ED-A326-560631FFA6D4"), 1
    ),
    "unusual_pellet_ccs_input90": AreaAnalyzeClass(
        uuid.UUID("A6DE849A-3C4E-482F-BDC7-6A8CB01CDCBF"), 1
    ),
    "unusual_pellet_ccs_input91": AreaAnalyzeClass(
        uuid.UUID("058E7BB2-4D16-4410-B30E-A3B557754C9D"), 1
    ),
    "unusual_pellet_ccs_input92": AreaAnalyzeClass(
        uuid.UUID("08A4FC8C-2A84-441C-9562-1683884A1209"), 1
    ),
    "unusual_pellet_ccs_input93": AreaAnalyzeClass(
        uuid.UUID("C2582ACE-BA54-498A-9ACB-26A79CD43733"), 1
    ),
    "unusual_pellet_ccs_input94": AreaAnalyzeClass(
        uuid.UUID("AB91964C-26B1-4AD3-B578-87B985C4354F"), 1
    ),
    "unusual_pellet_ccs_input95": AreaAnalyzeClass(
        uuid.UUID("A0DC9798-2792-47D2-B602-947108895AC1"), 1
    ),
    "unusual_pellet_ccs_input96": AreaAnalyzeClass(
        uuid.UUID("9324B364-7BDD-4EFC-8B3E-53F6A4D00FEC"), 1
    ),
    "unusual_pellet_ccs_input97": AreaAnalyzeClass(
        uuid.UUID("DB564CC7-FA5F-4CC6-92A9-FBEACA2CE5B8"), 1
    ),
    "unusual_pellet_ccs_input98": AreaAnalyzeClass(
        uuid.UUID("67754F7C-EFFC-4414-BE2D-E868DC1DD907"), 1
    ),
    "unusual_pellet_ccs_input99": AreaAnalyzeClass(
        uuid.UUID("7E05212C-C495-42F8-8F32-CCFF6AB76919"), 1
    ),
    "unusual_pellet_ccs_std": AreaAnalyzeClass(
        uuid.UUID("410DF073-CFAE-47F0-BDC4-146654760FC3"), 2
    ),
    "unusual_pellet_feo_avg": AreaAnalyzeClass(
        uuid.UUID("0E5E1388-A236-43C2-A9F6-83F92F0E6784"), 2
    ),
    "unusual_pellet_feo_input1": AreaAnalyzeClass(
        uuid.UUID("3E13C012-5467-4576-B0D0-5EE888857578"), 1
    ),
    "unusual_pellet_feo_input2": AreaAnalyzeClass(
        uuid.UUID("3B0A74F6-6BFB-4E8E-B764-04F7D2C122DC"), 1
    ),
    "unusual_pellet_moisture_input": AreaAnalyzeClass(
        uuid.UUID("8E7610AA-A77E-46D6-9871-52823BB0103F"), 1
    ),
    "unusual_pellet_porosity_dry": AreaAnalyzeClass(
        uuid.UUID("57C16C19-FB15-45E3-92E0-5FD339B64271"), 1
    ),
    "unusual_pellet_porosity_result": AreaAnalyzeClass(
        uuid.UUID("AD3185A7-5F01-4173-8FF0-0D94FB01B82F"), 2
    ),
    "unusual_pellet_porosity_saturated": AreaAnalyzeClass(
        uuid.UUID("2B55A470-ED77-4F96-A554-2AC9755CF097"), 1
    ),
    "unusual_pellet_porosity_suspended": AreaAnalyzeClass(
        uuid.UUID("5D25571A-FC36-4C86-88F4-B10A05EBF384"), 1
    ),
    "unusual_pellet_sievesize_12516mm": AreaAnalyzeClass(
        uuid.UUID("5629D507-1EA9-4A63-8D0B-5C1B2EE768B8"), 1
    ),
    "unusual_pellet_sievesize_12516w": AreaAnalyzeClass(
        uuid.UUID("489DFD4D-8DD6-44E5-B982-12B8F19DE136"), 2
    ),
    "unusual_pellet_sievesize_16mm": AreaAnalyzeClass(
        uuid.UUID("81C42031-756E-4057-A949-5CD92115BDCD"), 1
    ),
    "unusual_pellet_sievesize_16w": AreaAnalyzeClass(
        uuid.UUID("B8778B85-28AB-4BCA-823F-3D710040CB3F"), 2
    ),
    "unusual_pellet_sievesize_639mm": AreaAnalyzeClass(
        uuid.UUID("A69D3486-04B6-4190-B21B-62BBB92E5AA2"), 1
    ),
    "unusual_pellet_sievesize_639w": AreaAnalyzeClass(
        uuid.UUID("426F3780-6C22-4B40-9C45-8069BCA0DAFC"), 2
    ),
    "unusual_pellet_sievesize_63mm": AreaAnalyzeClass(
        uuid.UUID("14C0A8A9-DA6B-4A27-8B96-90232DF6217C"), 1
    ),
    "unusual_pellet_sievesize_63w": AreaAnalyzeClass(
        uuid.UUID("411185CB-F686-4881-8DE2-B6B3FA2D7645"), 2
    ),
    "unusual_pellet_sievesize_9125mm": AreaAnalyzeClass(
        uuid.UUID("8A33D494-CB72-4D6F-A997-C510DBF9526E"), 1
    ),
    "unusual_pellet_sievesize_9125w": AreaAnalyzeClass(
        uuid.UUID("70A47F7E-AD95-41EC-B2D9-DC6B20437156"), 2
    ),
    "unusual_pellet_sievesize_weight": AreaAnalyzeClass(
        uuid.UUID("9130BFA8-74F6-4508-B40A-8A735135EFC6"), 1
    ),
    "unusual_pellet_sulfur_input": AreaAnalyzeClass(
        uuid.UUID("F37C0005-15AE-426D-B71A-1FFED38708DA"), 1
    ),
    "unusual_pellet_tfe_avg": AreaAnalyzeClass(
        uuid.UUID("79B439BC-B118-4E79-B612-E6387A5FE13F"), 2
    ),
    "unusual_pellet_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("A4B9C5E6-3E7E-4138-81A3-32A7DE5DC259"), 1
    ),
    "unusual_pellet_tfe_input2": AreaAnalyzeClass(
        uuid.UUID("118B5537-9E22-4009-940C-D129047EC296"), 1
    ),
    "unusual_pellet_tumble_r5w": AreaAnalyzeClass(
        uuid.UUID("72C17629-9FAE-4B15-BC35-D8755459953C"), 2
    ),
    "unusual_pellet_tumble_r63w": AreaAnalyzeClass(
        uuid.UUID("500A7691-0CAF-4008-9681-6867BA64DF2C"), 2
    ),
    "unusual_pellet_tumble_remain5": AreaAnalyzeClass(
        uuid.UUID("DDD66373-F34E-4658-9E55-441FCDCC9AED"), 1
    ),
    "unusual_pellet_tumble_remain63": AreaAnalyzeClass(
        uuid.UUID("79EC6A44-0207-4CEF-A530-CD7FDBFCA91C"), 1
    ),
    "unusual_pellet_tumble_weight": AreaAnalyzeClass(
        uuid.UUID("C98B93A3-5346-4A7A-BACA-C2943A8701CE"), 1
    ),
    "unusual_pellet_xray_al2o3": AreaAnalyzeClass(
        uuid.UUID("E94799D2-9C6F-4772-A529-3D7821E1F923"), 1
    ),
    "unusual_pellet_xray_cao": AreaAnalyzeClass(
        uuid.UUID("1118172E-6A3C-4B60-AED3-80CF0390A5DD"), 1
    ),
    "unusual_pellet_xray_mgo": AreaAnalyzeClass(
        uuid.UUID("65B7660C-8140-4F87-B863-B959F1C719F6"), 1
    ),
    "unusual_pellet_xray_mno": AreaAnalyzeClass(
        uuid.UUID("456B48AE-6C10-4DEC-8B96-5A63264C430B"), 1
    ),
    "unusual_pellet_xray_p": AreaAnalyzeClass(
        uuid.UUID("24F474D9-74DB-44EB-B435-D3E9E3940CD8"), 1
    ),
    "unusual_pellet_xray_result": AreaAnalyzeClass(
        uuid.UUID("0BC3B41A-1A4D-44E6-AD50-D300AAC27776"), 2
    ),
    "unusual_pellet_xray_sio2": AreaAnalyzeClass(
        uuid.UUID("06D62ED0-9D4E-48D1-B218-990FABD81D4C"), 1
    ),
    "unusual_pellet_xray_tio2": AreaAnalyzeClass(
        uuid.UUID("E0D0A09B-AA8F-48EC-A935-5ED514614B68"), 1
    ),
    "unusual_unusual_atomic_k2o": AreaAnalyzeClass(
        uuid.UUID("5C3F244D-7C01-41D0-B022-EEC8B52C267A"), 1
    ),
    "unusual_unusual_atomic_na2o": AreaAnalyzeClass(
        uuid.UUID("809785F9-E370-4E79-A640-CD5DD498465D"), 1
    ),
    "unusual_unusual_bulkdensity_input": AreaAnalyzeClass(
        uuid.UUID("ABF18EF4-A648-4E9E-A094-139B8F0780E6"), 1
    ),
    "unusual_unusual_density_input": AreaAnalyzeClass(
        uuid.UUID("7E07654A-684F-4C11-82B7-E7C673E78096"), 1
    ),
    "unusual_unusual_loi_input": AreaAnalyzeClass(
        uuid.UUID("51EF108B-91C0-47C2-8C8F-75D77B706BBC"), 2
    ),
    "unusual_unusual_sg_input": AreaAnalyzeClass(
        uuid.UUID("A5763D3E-436C-4ED7-A6F0-CDF32A32A93A"), 1
    ),
    "unusual_unusual_sulfur_input": AreaAnalyzeClass(
        uuid.UUID("C4CE1A17-6CE5-403A-B3E8-C4BA043D4EE8"), 1
    ),
    "wateranalyze_cooling_ca2plus_input": AreaAnalyzeClass(
        uuid.UUID("AA085DDB-1051-41F9-83C0-7513CFA72806"), 1
    ),
    "wateranalyze_cooling_coponcr_alloydensity": AreaAnalyzeClass(
        uuid.UUID("FE229A60-DE30-4E7A-853C-F829FD5AEC46"), 1
    ),
    "wateranalyze_cooling_coponcr_exposedarea": AreaAnalyzeClass(
        uuid.UUID("C6865CB5-B877-464A-BA7A-1FFC23BA5A10"), 1
    ),
    "wateranalyze_cooling_coponcr_exposuretime": AreaAnalyzeClass(
        uuid.UUID("505C1993-0A03-4CFD-AFE3-4B75C2EEECBF"), 1
    ),
    "wateranalyze_cooling_coponcr_finallweight": AreaAnalyzeClass(
        uuid.UUID("1E33B4B7-84F7-41F1-B666-CB10D2548141"), 1
    ),
    "wateranalyze_cooling_coponcr_initialweight": AreaAnalyzeClass(
        uuid.UUID("94A78450-EACE-4028-AB95-9AD1C96DA24A"), 1
    ),
    "wateranalyze_cooling_coponcr_result": AreaAnalyzeClass(
        uuid.UUID("8F39B199-1D6C-44AE-8DC5-E3FC81A4D1E8"), 2
    ),
    "wateranalyze_cooling_corraterinstrument_input": AreaAnalyzeClass(
        uuid.UUID("2376E666-C212-49B1-8472-E9428F6C218A"), 1
    ),
    "wateranalyze_cooling_ec_input": AreaAnalyzeClass(
        uuid.UUID("83504124-A082-42BF-94B1-F2124CD4F7AC"), 1
    ),
    "wateranalyze_cooling_mg2plus_input": AreaAnalyzeClass(
        uuid.UUID("FF951F2B-24B1-4C70-A618-25689860B7F3"), 1
    ),
    "wateranalyze_cooling_no2_input": AreaAnalyzeClass(
        uuid.UUID("28716049-3138-4725-A8F2-34E982AEC426"), 1
    ),
    "wateranalyze_cooling_no3_input": AreaAnalyzeClass(
        uuid.UUID("83517364-6812-4A8A-97A8-C21C95D1A77D"), 1
    ),
    "wateranalyze_cooling_opo43_input": AreaAnalyzeClass(
        uuid.UUID("56768F3E-BBE6-4552-BE15-EDDBE7BC56F4"), 1
    ),
    "wateranalyze_cooling_ph_input": AreaAnalyzeClass(
        uuid.UUID("88125475-ED28-4B3A-A49F-CE0B3A63C9AE"), 1
    ),
    "wateranalyze_cooling_salinity_input": AreaAnalyzeClass(
        uuid.UUID("DF7BF50A-2510-41C2-86DA-CD36CE36D5B1"), 1
    ),
    "wateranalyze_cooling_srb_input1": AreaAnalyzeClass(
        uuid.UUID("ABCB3BC6-7C8A-4FA3-B497-711441243DD3"), 1
    ),
    "wateranalyze_cooling_srb_input2": AreaAnalyzeClass(
        uuid.UUID("278BC3C1-F9BA-44E8-B29F-5F86C30513B3"), 1
    ),
    "wateranalyze_cooling_t_input": AreaAnalyzeClass(
        uuid.UUID("6EB9D4F5-E263-463B-B5DB-477726E929C8"), 1
    ),
    "wateranalyze_cooling_tbc_input": AreaAnalyzeClass(
        uuid.UUID("4454212B-029B-465C-8370-2516A463A272"), 1
    ),
    "wateranalyze_cooling_tbc_result": AreaAnalyzeClass(
        uuid.UUID("3822DC0C-6DB4-470C-9CC4-1B12AFB63EB9"), 2
    ),
    "wateranalyze_cooling_tds_input": AreaAnalyzeClass(
        uuid.UUID("7662D420-3E09-4AC3-9E8E-878A7866E451"), 1
    ),
    "wateranalyze_cooling_th_input": AreaAnalyzeClass(
        uuid.UUID("3EC7D3AC-EB4C-4CF8-9B5A-11A8834BF41D"), 1
    ),
    "wateranalyze_cooling_tpo43_input": AreaAnalyzeClass(
        uuid.UUID("D9CBA301-DD00-4D07-A410-AA813FE6D0EE"), 1
    ),
    "wateranalyze_cooling_ts_result": AreaAnalyzeClass(
        uuid.UUID("E563164C-33DA-447C-BF21-7C3739E10BAF"), 2
    ),
    "wateranalyze_cooling_ts_tds": AreaAnalyzeClass(
        uuid.UUID("06AD92FB-FFF6-43D3-B7B8-88F73B8941C3"), 1
    ),
    "wateranalyze_cooling_ts_tss": AreaAnalyzeClass(
        uuid.UUID("F89CC69C-DB68-45E7-AAF4-FC8EAB30270B"), 1
    ),
    "wateranalyze_cooling_tss_input": AreaAnalyzeClass(
        uuid.UUID("A5BABBC5-C54E-42D0-BF7A-DEB44BEE2666"), 1
    ),
    "wateranalyze_cooling_turbidity_input": AreaAnalyzeClass(
        uuid.UUID("AFD61C0A-740C-42FD-9EA8-BDC031B28823"), 1
    ),
    "wateranalyze_hpgrclose_ec_input": AreaAnalyzeClass(
        uuid.UUID("EBFCABD9-530A-45A5-A1FC-A2D7C012F7DB"), 1
    ),
    "wateranalyze_hpgrclose_no2_input": AreaAnalyzeClass(
        uuid.UUID("A92ACEC9-1608-45D8-A4C8-A31EF6B53770"), 1
    ),
    "wateranalyze_hpgrclose_no3_input": AreaAnalyzeClass(
        uuid.UUID("D4564BA9-3CFB-44C5-BC97-73B035D6B93E"), 1
    ),
    "wateranalyze_hpgrclose_opo43_input": AreaAnalyzeClass(
        uuid.UUID("6E617B52-4501-4B5E-B1DC-EA2A5ECFF714"), 1
    ),
    "wateranalyze_hpgrclose_ph_input": AreaAnalyzeClass(
        uuid.UUID("9570ACE7-4130-4217-9298-805715C6BC53"), 1
    ),
    "wateranalyze_hpgrclose_t_input": AreaAnalyzeClass(
        uuid.UUID("3995572C-39B3-449C-8DD7-6580F67DCE76"), 1
    ),
    "wateranalyze_hpgrclose_th_input": AreaAnalyzeClass(
        uuid.UUID("E2679317-752C-4C2A-A857-1DF2D6F0696B"), 1
    ),
    "wateranalyze_hpgrclose_tpo43_input": AreaAnalyzeClass(
        uuid.UUID("1BA9B4F8-6CF0-4C8F-BDCE-D6D0B1B41004"), 1
    ),
    "wateranalyze_hpgropen_ec_input": AreaAnalyzeClass(
        uuid.UUID("15682FA9-1AD7-4E85-9B70-16311AE6C6BB"), 1
    ),
    "wateranalyze_hpgropen_no2_input": AreaAnalyzeClass(
        uuid.UUID("E0BB8665-68DE-4CA0-9225-69D1E162A9C6"), 1
    ),
    "wateranalyze_hpgropen_no3_input": AreaAnalyzeClass(
        uuid.UUID("4806F841-568F-4538-8862-65748413B517"), 1
    ),
    "wateranalyze_hpgropen_opo43_input": AreaAnalyzeClass(
        uuid.UUID("5D862576-DDA8-4055-92E7-249570E70861"), 1
    ),
    "wateranalyze_hpgropen_ph_input": AreaAnalyzeClass(
        uuid.UUID("28AF1B82-C0A1-428A-B744-40B9516105E7"), 1
    ),
    "wateranalyze_hpgropen_t_input": AreaAnalyzeClass(
        uuid.UUID("9042D695-C7D5-4F47-90CD-05451EF157E8"), 1
    ),
    "wateranalyze_hpgropen_th_input": AreaAnalyzeClass(
        uuid.UUID("7EC32CA9-FFE6-4889-9DDE-4133C902B1EA"), 1
    ),
    "wateranalyze_hpgropen_tpo43_input": AreaAnalyzeClass(
        uuid.UUID("974480AE-363B-4790-8F5C-B9DB9F6A40ED"), 1
    ),
    "wateranalyze_makeup_ca2plus_input": AreaAnalyzeClass(
        uuid.UUID("E060F656-BC48-4686-A367-B13F8C2F74FB"), 1
    ),
    "wateranalyze_makeup_cl_input": AreaAnalyzeClass(
        uuid.UUID("8345F24F-1FF0-4F2D-A6A3-8F2AA2FAAA73"), 1
    ),
    "wateranalyze_makeup_ec_input": AreaAnalyzeClass(
        uuid.UUID("EF1A1AEC-734F-4B46-AF21-B191B85EE96E"), 1
    ),
    "wateranalyze_makeup_malk_input": AreaAnalyzeClass(
        uuid.UUID("788631C4-3418-4923-90D7-F7A1D68C0BBE"), 1
    ),
    "wateranalyze_makeup_mg2plus_input": AreaAnalyzeClass(
        uuid.UUID("71568125-AB5D-4A51-A1EB-63495DF39DAF"), 1
    ),
    "wateranalyze_makeup_no2_input": AreaAnalyzeClass(
        uuid.UUID("930065B3-E8A2-48FE-861F-0C473EA2C887"), 1
    ),
    "wateranalyze_makeup_no3_input": AreaAnalyzeClass(
        uuid.UUID("8496E453-46A4-4DEF-9C42-F861B01DA434"), 1
    ),
    "wateranalyze_makeup_palk_input": AreaAnalyzeClass(
        uuid.UUID("E8C5ABFF-FF1C-4F46-8A50-7517E73CFF85"), 1
    ),
    "wateranalyze_makeup_ph_input": AreaAnalyzeClass(
        uuid.UUID("AC646B8D-2EE9-4A62-B7A6-49998B9079AC"), 1
    ),
    "wateranalyze_makeup_salinity_input": AreaAnalyzeClass(
        uuid.UUID("07A8E003-ADF5-4905-A1D9-4844FA8E3085"), 1
    ),
    "wateranalyze_makeup_so42_input": AreaAnalyzeClass(
        uuid.UUID("26E9A5AA-8916-46D4-82F3-EE52AF9A6340"), 1
    ),
    "wateranalyze_makeup_t_input": AreaAnalyzeClass(
        uuid.UUID("39F4B7C4-9D8F-4FD1-82E8-A3E52FCA417F"), 1
    ),
    "wateranalyze_makeup_tds_input": AreaAnalyzeClass(
        uuid.UUID("00B8A63A-6FCF-455B-86CF-58185AE0A8C9"), 1
    ),
    "wateranalyze_makeup_th_input": AreaAnalyzeClass(
        uuid.UUID("547526BA-24A9-4FD1-B48E-1B548E26E42A"), 1
    ),
    "wateranalyze_makeup_ts_result": AreaAnalyzeClass(
        uuid.UUID("7E09069A-90A5-4176-9007-B140D81D2280"), 2
    ),
    "wateranalyze_makeup_ts_tds": AreaAnalyzeClass(
        uuid.UUID("964D0114-8C3C-43EA-B6D2-525A242B72C4"), 1
    ),
    "wateranalyze_makeup_ts_tss": AreaAnalyzeClass(
        uuid.UUID("98EC120C-4A0D-4B7D-913A-0D19690568A7"), 1
    ),
    "wateranalyze_makeup_tss_input": AreaAnalyzeClass(
        uuid.UUID("C4DF12AD-4E94-4690-BF16-3AC31415FCEE"), 1
    ),
    "wateranalyze_makeup_turbidity_input": AreaAnalyzeClass(
        uuid.UUID("A46BF238-8A88-4A2E-BCCC-4211C3549165"), 1
    ),
    "wateranalyze_potable_ca2plus_input": AreaAnalyzeClass(
        uuid.UUID("ABC8CC4A-3C7C-4797-BCD6-810690060665"), 1
    ),
    "wateranalyze_potable_cl_input": AreaAnalyzeClass(
        uuid.UUID("76A2EF6D-40AB-4DAF-9098-9B746A1F57E4"), 1
    ),
    "wateranalyze_potable_ec_input": AreaAnalyzeClass(
        uuid.UUID("A502EA05-DBEC-4B15-B65B-E12D48925858"), 1
    ),
    "wateranalyze_potable_fcl2_input": AreaAnalyzeClass(
        uuid.UUID("647C2061-5EF8-48DC-9E0B-0F968277B8C4"), 1
    ),
    "wateranalyze_potable_malk_input": AreaAnalyzeClass(
        uuid.UUID("7520003A-C33A-4B62-8FBE-27A24A288AF8"), 1
    ),
    "wateranalyze_potable_mg2plus_input": AreaAnalyzeClass(
        uuid.UUID("05C0AEF5-3410-47F6-AE6C-41306F5C1DC3"), 1
    ),
    "wateranalyze_potable_no2_input": AreaAnalyzeClass(
        uuid.UUID("3F145849-8D97-4B27-8746-EBAC6BD562F6"), 1
    ),
    "wateranalyze_potable_no3_input": AreaAnalyzeClass(
        uuid.UUID("3EA4CD09-D94E-4AC5-98DA-CE1BD460BBF0"), 1
    ),
    "wateranalyze_potable_palk_input": AreaAnalyzeClass(
        uuid.UUID("80D3C1FA-4A95-45CE-B031-45C11E0E0D44"), 1
    ),
    "wateranalyze_potable_ph_input": AreaAnalyzeClass(
        uuid.UUID("0FCC7804-3CBF-4F84-A797-EAC80C816C64"), 1
    ),
    "wateranalyze_potable_salinity_input": AreaAnalyzeClass(
        uuid.UUID("1517D5A1-4F88-4197-8C71-01D8C9855A82"), 1
    ),
    "wateranalyze_potable_so42_input": AreaAnalyzeClass(
        uuid.UUID("26568A8E-F9AA-4B44-B74C-31243359E53C"), 1
    ),
    "wateranalyze_potable_t_input": AreaAnalyzeClass(
        uuid.UUID("84152C8E-F179-453D-97F8-E44B6260A0CA"), 1
    ),
    "wateranalyze_potable_tds_input": AreaAnalyzeClass(
        uuid.UUID("13D36331-DF8E-4A44-8B2B-B2BB5A417C63"), 1
    ),
    "wateranalyze_potable_th_input": AreaAnalyzeClass(
        uuid.UUID("2AFF5D3A-1AAE-4456-9A98-01D5CB5C4750"), 1
    ),
    "wateranalyze_potable_ts_result": AreaAnalyzeClass(
        uuid.UUID("62321F37-66BD-4697-ACDA-241E9A80F62C"), 2
    ),
    "wateranalyze_potable_ts_tds": AreaAnalyzeClass(
        uuid.UUID("5525CA4E-5E1B-47CA-82CF-78F6422C0C1D"), 1
    ),
    "wateranalyze_potable_ts_tss": AreaAnalyzeClass(
        uuid.UUID("2D60847A-340C-4761-B58C-11B3DA060F56"), 1
    ),
    "wateranalyze_potable_tss_input": AreaAnalyzeClass(
        uuid.UUID("147D86BE-3067-4C24-BB18-AFCD65B7C12A"), 1
    ),
    "wateranalyze_potable_turbidity_input": AreaAnalyzeClass(
        uuid.UUID("565D4258-C8F1-4E2A-AB97-07D24C642B1B"), 1
    ),
    "wateranalyze_process_ca2plus_input": AreaAnalyzeClass(
        uuid.UUID("D9E8023C-F525-4D00-95A1-68AD4252317C"), 1
    ),
    "wateranalyze_process_cl_input": AreaAnalyzeClass(
        uuid.UUID("FBA1AA10-15D4-482E-86CE-13D1EB20F7EE"), 1
    ),
    "wateranalyze_process_cod_input": AreaAnalyzeClass(
        uuid.UUID("3FF5350E-8BD3-4C49-8047-6A598491939A"), 1
    ),
    "wateranalyze_process_ec_input": AreaAnalyzeClass(
        uuid.UUID("081B6475-80D2-42E0-959B-FC98795D8D55"), 1
    ),
    "wateranalyze_process_f_input": AreaAnalyzeClass(
        uuid.UUID("EE9BCFB5-CF1D-4E77-9A6E-AA362EFFE747"), 1
    ),
    "wateranalyze_process_malk_input": AreaAnalyzeClass(
        uuid.UUID("A25BE5C1-3D3A-4B78-AFF3-CC03B06CFF76"), 1
    ),
    "wateranalyze_process_mg2plus_input": AreaAnalyzeClass(
        uuid.UUID("4AA35F5C-1907-4FA8-B04F-C0C8328A689F"), 1
    ),
    "wateranalyze_process_no2_input": AreaAnalyzeClass(
        uuid.UUID("5CC82D81-5747-4517-8A32-6DB183A5E129"), 1
    ),
    "wateranalyze_process_no3_input": AreaAnalyzeClass(
        uuid.UUID("970C189C-DF12-4DC6-99B1-3CBC790E33DD"), 1
    ),
    "wateranalyze_process_palk_input": AreaAnalyzeClass(
        uuid.UUID("4C4B105A-FA0B-4EC9-A195-0B308E70F038"), 1
    ),
    "wateranalyze_process_ph_input": AreaAnalyzeClass(
        uuid.UUID("2625130E-6212-4785-9039-9C85A2B76303"), 1
    ),
    "wateranalyze_process_salinity_input": AreaAnalyzeClass(
        uuid.UUID("789288E7-436B-4FDF-AAB8-EE02E1B028D4"), 1
    ),
    "wateranalyze_process_sio2_input": AreaAnalyzeClass(
        uuid.UUID("548DB5A5-7039-4982-B65C-DEC192FDABEC"), 1
    ),
    "wateranalyze_process_so42_input": AreaAnalyzeClass(
        uuid.UUID("A76ABD61-5418-4EF7-B71B-48EDC91E63DC"), 1
    ),
    "wateranalyze_process_t_input": AreaAnalyzeClass(
        uuid.UUID("340A4694-814F-4F17-97F2-72ED89FF2CFB"), 1
    ),
    "wateranalyze_process_tds_input": AreaAnalyzeClass(
        uuid.UUID("C046A316-19E2-4191-BEC9-7D4774BAFEFC"), 1
    ),
    "wateranalyze_process_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("7E4637D2-CC61-486D-AB8D-967EB9313D91"), 1
    ),
    "wateranalyze_process_th_input": AreaAnalyzeClass(
        uuid.UUID("326CFBF1-6505-4452-B5FB-F6B13EC81F50"), 1
    ),
    "wateranalyze_process_ts_input": AreaAnalyzeClass(
        uuid.UUID("9B3611C6-78EC-477D-8982-1C5910DDE247"), 1
    ),
    "wateranalyze_process_ts_result": AreaAnalyzeClass(
        uuid.UUID("3F388499-258D-4854-A3C9-11E031A15F1F"), 2
    ),
    "wateranalyze_process_ts_tds": AreaAnalyzeClass(
        uuid.UUID("A219B1CF-E294-45DC-B9DE-865575DD7170"), 1
    ),
    "wateranalyze_process_ts_tss": AreaAnalyzeClass(
        uuid.UUID("B8E14CB9-9DAF-496F-A33E-E738AEB0A182"), 1
    ),
    "wateranalyze_process_tss_input": AreaAnalyzeClass(
        uuid.UUID("B4A6E165-A683-4907-B4F0-486F5B1DD2C6"), 1
    ),
    "wateranalyze_softener1_ec_input": AreaAnalyzeClass(
        uuid.UUID("3963D6C9-633B-425F-8645-FFD03C52E8DC"), 1
    ),
    "wateranalyze_softener1_ph_input": AreaAnalyzeClass(
        uuid.UUID("A303C809-063D-4D52-B0ED-8C5092B1A6F4"), 1
    ),
    "wateranalyze_softener1_t_input": AreaAnalyzeClass(
        uuid.UUID("A7AB957D-206F-4356-9A09-9FDE21001185"), 1
    ),
    "wateranalyze_softener1_th_input": AreaAnalyzeClass(
        uuid.UUID("00F485F9-372A-4149-B063-73507C122A80"), 1
    ),
    "wateranalyze_softener2_ec_input": AreaAnalyzeClass(
        uuid.UUID("E61CE591-1854-454E-A128-4ED02330B2AE"), 1
    ),
    "wateranalyze_softener2_ph_input": AreaAnalyzeClass(
        uuid.UUID("608277DA-BBC6-4D0E-B0D3-D2713C5604B2"), 1
    ),
    "wateranalyze_softener2_t_input": AreaAnalyzeClass(
        uuid.UUID("F0C177FB-CE2D-47B4-AAAC-B77623265FC1"), 1
    ),
    "wateranalyze_softener2_th_input": AreaAnalyzeClass(
        uuid.UUID("9234C5CB-8712-4C60-9D88-7CFA86691FBD"), 1
    ),
    "wateranalyze_spirometer_ec_input": AreaAnalyzeClass(
        uuid.UUID("0FB864A8-3955-4C05-A509-F28B5C8DAF36"), 1
    ),
    "wateranalyze_spirometer_no2_input": AreaAnalyzeClass(
        uuid.UUID("D35483F8-50C4-4108-B239-F9FEB836450A"), 1
    ),
    "wateranalyze_spirometer_no3_input": AreaAnalyzeClass(
        uuid.UUID("80DD6FE1-A862-40D8-BA06-00EC80EA7460"), 1
    ),
    "wateranalyze_spirometer_opo43_input": AreaAnalyzeClass(
        uuid.UUID("FA5AF9CD-8C0A-4BD0-BC14-13D95D173CB1"), 1
    ),
    "wateranalyze_spirometer_ph_input": AreaAnalyzeClass(
        uuid.UUID("44DA8C78-0E33-498F-A636-A1C19ACE4A14"), 1
    ),
    "wateranalyze_spirometer_t_input": AreaAnalyzeClass(
        uuid.UUID("2F5F364E-45D7-4DAF-9DC1-6A5317C75951"), 1
    ),
    "wateranalyze_spirometer_th_input": AreaAnalyzeClass(
        uuid.UUID("82C885C7-38DD-4DED-B28F-E4C7B20B19D5"), 1
    ),
    "wateranalyze_spirometer_tpo43_input": AreaAnalyzeClass(
        uuid.UUID("6BCB9E27-56E2-46C7-899A-F3D20FF9660C"), 1
    ),
    "wateranalyze_unknown_ca2plus_input": AreaAnalyzeClass(
        uuid.UUID("99279117-5D9C-4122-B4E4-52EE8F363007"), 1
    ),
    "wateranalyze_unknown_cl_input": AreaAnalyzeClass(
        uuid.UUID("1B4C4A34-A36B-4B5C-BF36-4C8D8BDB2645"), 1
    ),
    "wateranalyze_unknown_cod_input": AreaAnalyzeClass(
        uuid.UUID("729C5E15-70B3-42F6-BCBE-2281004E48D1"), 1
    ),
    "wateranalyze_unknown_ec_input": AreaAnalyzeClass(
        uuid.UUID("12C91D7B-6A83-41FD-9F7A-1607D74AF11F"), 1
    ),
    "wateranalyze_unknown_malk_input": AreaAnalyzeClass(
        uuid.UUID("5D460E89-B919-4193-AF32-2BD6EF62E2AD"), 1
    ),
    "wateranalyze_unknown_mg2plus_input": AreaAnalyzeClass(
        uuid.UUID("96EE9763-EBDC-444F-ACA4-FD9EFD70BF4A"), 1
    ),
    "wateranalyze_unknown_no3_input": AreaAnalyzeClass(
        uuid.UUID("BC2591E1-BE76-4AEF-B87D-486C66B9736A"), 1
    ),
    "wateranalyze_unknown_palk_input": AreaAnalyzeClass(
        uuid.UUID("B98559AC-B609-4D31-889D-7BB75D10F5B2"), 1
    ),
    "wateranalyze_unknown_ph_input": AreaAnalyzeClass(
        uuid.UUID("6243ADBC-94F5-444F-BCE4-4560C38CE17E"), 1
    ),
    "wateranalyze_unknown_salinity_input": AreaAnalyzeClass(
        uuid.UUID("A2C544DE-7A6F-4BBB-90F8-E1BEA0FA71B0"), 1
    ),
    "wateranalyze_unknown_so42_input": AreaAnalyzeClass(
        uuid.UUID("45F5C198-6C1E-44B9-A808-CB3CE6D98C75"), 1
    ),
    "wateranalyze_unknown_t_input": AreaAnalyzeClass(
        uuid.UUID("A916E1A2-902C-407A-805C-8F39059A37CD"), 1
    ),
    "wateranalyze_unknown_tds_input": AreaAnalyzeClass(
        uuid.UUID("8537E5A7-EDFE-45BB-8EBC-5F8AC60EB708"), 1
    ),
    "wateranalyze_unknown_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("E079443E-CBB5-4A08-B6E8-2BC6F897A996"), 1
    ),
    "wateranalyze_unknown_th_input": AreaAnalyzeClass(
        uuid.UUID("7D09E2B0-313C-4098-8CFA-CFF408043982"), 1
    ),
    "wateranalyze_unknown_tpo43_input": AreaAnalyzeClass(
        uuid.UUID("29D21DAB-8272-45B4-88EB-F4BC3EFB830B"), 1
    ),
    "wateranalyze_unknown_ts_result": AreaAnalyzeClass(
        uuid.UUID("A6018641-B0CC-4C29-BCD5-0DBA10A16476"), 2
    ),
    "wateranalyze_unknown_ts_tds": AreaAnalyzeClass(
        uuid.UUID("D2B276BD-4829-482B-9CB9-5AD53BB8881C"), 1
    ),
    "wateranalyze_unknown_ts_tss": AreaAnalyzeClass(
        uuid.UUID("31F74F91-54CB-4B29-8FA1-73D5ADBA45DD"), 1
    ),
    "wateranalyze_unknown_tss_input": AreaAnalyzeClass(
        uuid.UUID("9E9D086B-478D-43E1-B713-AE9CADE3AE4C"), 1
    ),
    "wateranalyze_unknown_turbidity_input": AreaAnalyzeClass(
        uuid.UUID("D80F1B8B-66AB-4611-BD6E-1D66C6822FE4"), 1
    ),
    "wateranalyze_unusual_bod_input": AreaAnalyzeClass(
        uuid.UUID("D9D97D47-2DD0-436E-8FD7-EBFB1E50A1A5"), 1
    ),
    "wateranalyze_unusual_cod_input": AreaAnalyzeClass(
        uuid.UUID("0B9A01D8-A42A-43B0-A7CA-57B95D2C2830"), 1
    ),
    "wateranalyze_unusual_do_input": AreaAnalyzeClass(
        uuid.UUID("BF821BBF-9ACA-45EC-98BD-19E9FAF66692"), 1
    ),
    "wateranalyze_unusual_f_input": AreaAnalyzeClass(
        uuid.UUID("D6409EDE-90BD-433B-9FB7-449482501285"), 1
    ),
    "wateranalyze_unusual_k_input": AreaAnalyzeClass(
        uuid.UUID("50284D27-33E6-46B1-A0C4-5ADA8E075D83"), 1
    ),
    "wateranalyze_unusual_na_input": AreaAnalyzeClass(
        uuid.UUID("E309799C-2935-4ABC-B82C-3FAFFE810427"), 1
    ),
    "wateranalyze_unusual_no2_input": AreaAnalyzeClass(
        uuid.UUID("A1FB800C-A837-45E6-9BE9-463B93217C26"), 1
    ),
    "wateranalyze_unusual_no3_input": AreaAnalyzeClass(
        uuid.UUID("41DEB25A-9592-470F-B4B9-13ACA80C3DE1"), 1
    ),
    "wateranalyze_unusual_orp_input": AreaAnalyzeClass(
        uuid.UUID("E60919FF-2557-48E6-9EEC-F85151FCFF1A"), 1
    ),
    "wateranalyze_unusual_sio2_input": AreaAnalyzeClass(
        uuid.UUID("6B6EC19E-F7BF-4DD3-AA8A-F235B6ADB1C4"), 1
    ),
    "wateranalyze_unusual_so32_input": AreaAnalyzeClass(
        uuid.UUID("4F21F2D5-4DB4-4AAC-A8FA-43F30D035CE0"), 1
    ),
    "wateranalyze_unusual_tfe_input1": AreaAnalyzeClass(
        uuid.UUID("76C2A9E2-0BD4-400E-938C-6A80A611D37E"), 1
    ),
    "wateranalyze_vacuumpump1_ec_input": AreaAnalyzeClass(
        uuid.UUID("5B49BF2D-F1D7-4609-AB87-D44AF5EF279B"), 1
    ),
    "wateranalyze_vacuumpump1_no2_input": AreaAnalyzeClass(
        uuid.UUID("D6CC7CAD-82C3-45BE-B2DD-ECBEDEEF55B0"), 1
    ),
    "wateranalyze_vacuumpump1_no3_input": AreaAnalyzeClass(
        uuid.UUID("0DE449B1-68AD-469B-A30A-71EE3205588F"), 1
    ),
    "wateranalyze_vacuumpump1_opo43_input": AreaAnalyzeClass(
        uuid.UUID("DFE5A0A3-FD97-408A-BE69-29C493AF7E81"), 1
    ),
    "wateranalyze_vacuumpump1_ph_input": AreaAnalyzeClass(
        uuid.UUID("62032D88-E360-4289-815E-7BE5CA2D4E32"), 1
    ),
    "wateranalyze_vacuumpump1_t_input": AreaAnalyzeClass(
        uuid.UUID("D45CAE2D-EAE2-486B-BB05-EE0576C92277"), 1
    ),
    "wateranalyze_vacuumpump1_th_input": AreaAnalyzeClass(
        uuid.UUID("37345763-18EE-4EEA-8B7C-73676B952D26"), 1
    ),
    "wateranalyze_vacuumpump1_tpo43_input": AreaAnalyzeClass(
        uuid.UUID("0C9B81F6-78D7-4E97-A4F3-BA61B1B93B22"), 1
    ),
    "wateranalyze_vacuumpump2_ec_input": AreaAnalyzeClass(
        uuid.UUID("A1A24140-FEEB-4193-BD9A-41B3AF386CD7"), 1
    ),
    "wateranalyze_vacuumpump2_no2_input": AreaAnalyzeClass(
        uuid.UUID("C6C49A8B-D023-47D1-91C6-7F107C26951F"), 1
    ),
    "wateranalyze_vacuumpump2_no3_input": AreaAnalyzeClass(
        uuid.UUID("E214CDF7-4A16-4E99-8681-E28E79AFD2D5"), 1
    ),
    "wateranalyze_vacuumpump2_opo43_input": AreaAnalyzeClass(
        uuid.UUID("EF1CD06B-CB43-4CA1-9079-8D7977D0CD75"), 1
    ),
    "wateranalyze_vacuumpump2_ph_input": AreaAnalyzeClass(
        uuid.UUID("5BA0F479-5842-4A35-8ED6-E7B7966EBEBA"), 1
    ),
    "wateranalyze_vacuumpump2_t_input": AreaAnalyzeClass(
        uuid.UUID("65BC16E4-AC2E-497B-AE1E-79C029E2A1C4"), 1
    ),
    "wateranalyze_vacuumpump2_th_input": AreaAnalyzeClass(
        uuid.UUID("9AB28712-44C0-4139-9624-041C9BCA3BCC"), 1
    ),
    "wateranalyze_vacuumpump2_tpo43_input": AreaAnalyzeClass(
        uuid.UUID("47780815-6F87-4C1A-BDDA-B000BA59BA33"), 1
    ),
}

areaAnalyzeIdToName = {v.areaAnalyzeID: k for k, v in areaAnalyzeIds.items()}

getAttrHtmName = {
    # 'beforemix_xrays': '',
    "aftermix_moisture510bc1s": "area500_aftermix_moisture_input",
    "beforemix_moisture500s": "area500_beforemix_moisture_input",
    "beforemix_tfes": "area500_beforemix_tfe_avg",
    "beforemix_feos": "area500_beforemix_feo_avg",
    "beforemix_sulfors": "area500_beforemix_sulfur_input",
    "beforemix_belines": "area500_beforemix_blaine_result",
    "wf1_feos": "area500_wf1_feo_avg",
    "wf2_feos": "area500_wf2_feo_avg",
    "wf3_feos": "area500_wf3_feo_avg",
    "wf4_feos": "area500_wf4_feo_avg",
    "wf5_feos": "area500_wf5_feo_avg",
    "wf6_feos": "area500_wf6_feo_avg",
    "wf7_feos": "area500_wf7_feo_avg",
    "wf8_feos": "area500_wf8_feo_avg",
    "wf9_feos": "area500_wf9_feo_avg",
    "wf10_feos": "area500_wf10_feo_avg",
    "wf1_moistures": "area500_wf1_moisture_input",
    "wf2_moistures": "area500_wf2_moisture_input",
    "wf3_moistures": "area500_wf3_moisture_input",
    "wf4_moistures": "area500_wf4_moisture_input",
    "wf5_moistures": "area500_wf5_moisture_input",
    "wf6_moistures": "area500_wf6_moisture_input",
    "wf7_moistures": "area500_wf7_moisture_input",
    "wf8_moistures": "area500_wf8_moisture_input",
    "wf9_moistures": "area500_wf9_moisture_input",
    "wf10_moistures": "area500_wf10_moisture_input",
    "wf1_belines": "area500_wf1_blaine_result",
    "wf2_belines": "area500_wf2_blaine_result",
    "wf3_belines": "area500_wf3_blaine_result",
    "wf4_belines": "area500_wf4_blaine_result",
    "wf5_belines": "area500_wf5_blaine_result",
    "wf6_belines": "area500_wf6_blaine_result",
    "wf7_belines": "area500_wf7_blaine_result",
    "wf8_belines": "area500_wf8_blaine_result",
    "wf9_belines": "area500_wf9_blaine_result",
    "wf10_belines": "area500_wf10_blaine_result",
    "wf1_tfes": "area500_wf1_tfe_avg",
    "wf2_tfes": "area500_wf2_tfe_avg",
    "wf3_tfes": "area500_wf3_tfe_avg",
    "wf4_tfes": "area500_wf4_tfe_avg",
    "wf5_tfes": "area500_wf5_tfe_avg",
    "wf6_tfes": "area500_wf6_tfe_avg",
    "wf7_tfes": "area500_wf7_tfe_avg",
    "wf8_tfes": "area500_wf8_tfe_avg",
    "wf9_tfes": "area500_wf9_tfe_avg",
    "wf10_tfes": "area500_wf10_tfe_avg",
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
        message = ""
        for name, value in self.__dict__.items():
            if value and isinstance(value, list):
                message += f"len({name})={len(value)} "
        return message if message else "Empty"

    def __iter__(self):
        for attribute_name, value in self.__dict__.items():
            if value and isinstance(value, list):
                yield attribute_name, value

            # if isinstance(value, list):
            #     yield attribute_name, value

    def has_any_list_with_value(self):
        pass
        # return any(value for value in self.__dict__.values() if value)
