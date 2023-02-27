from sqlalchemy import VARCHAR, DATE, NUMERIC

# Variables extracted from docs/metadata/SINAN files with converted to sqlalchemy types
COLUMN_TYPE = {
    "ANT_IDADE": NUMERIC(3),
    "ANT_RACA": VARCHAR(1),
    "ID_OCUPA_N": VARCHAR(6),
    "ESCOLMAE": VARCHAR(2),
    "ANT_PRE_NA": VARCHAR(1),
    "UF_PRE_NAT": VARCHAR(2),
    "MUN_PRE_NA": VARCHAR(6),
    "UNI_PRE_NA": VARCHAR(7),
    "ANTSIFIL_N": VARCHAR(1),
    "LAB_PARTO": VARCHAR(1),
    "LAB_TITU_2": NUMERIC(4),
    "LAB_DT3": DATE,
    "LAB_CONF": VARCHAR(1),
    "TRA_ESQUEM": VARCHAR(2),
    "TRA_DT": DATE,
    "ANT_TRATAD": VARCHAR(1),
    "ANT_UF_CRI": VARCHAR(2),
    "ANT_MUNI_C": VARCHAR(6),
    "ANT_LOCAL_": NUMERIC((8,0)),
    "LABC_SANGU": VARCHAR(1),
    "LABC_TIT_1": NUMERIC(4),
    "LABC_DT_1": DATE,
    "LABC_IGG": VARCHAR(1),
    "LABC_DT": DATE,
    "LABC_LIQUO": VARCHAR(1),
    "LABC_TIT_2": NUMERIC(4),
    "LABC_DT_2": DATE,
    "LABC_TITUL": VARCHAR(1),
    "LABC_EVIDE": VARCHAR(1),
    "LABC_LIQ_1": VARCHAR(1),
    "TRA_DIAG_T": VARCHAR(1),
    "CLI_ASSINT": VARCHAR(1),
    "CLI_ICTERI": VARCHAR(1),
    "CLI_ANEMIA": VARCHAR(1),
    "CLI_ESPLEN": VARCHAR(1),
    "CLI_OSTEO": VARCHAR(1),
    "CLI_RINITE": VARCHAR(1),
    "HEPATO": VARCHAR(1),
    "LESOES": VARCHAR(1),
    "CLI_PSEUDO": VARCHAR(1),
    "CLI_OUTRO": VARCHAR(1),
    "SIN_OUTR_E": VARCHAR(20),
    "TRA_ESQU_1": VARCHAR(1),
    "DS_ESQUEMA": VARCHAR(30),
    "EVOLUCAO": VARCHAR(1),
    "EVO_DIAG_N": VARCHAR(1),
    "DT_OBITO": DATE,
    "DT_INVEST": DATE,
    "ANT_UF_1": VARCHAR(2),
    "MUN_1": VARCHAR(6),
    "ANT_UF_2": VARCHAR(2),
    "MUN_2": VARCHAR(6),
    "ANT_UF_3": VARCHAR(2),
    "MUN_3": VARCHAR(6),
    "PRESENCA": VARCHAR(1),
    "PARASITO": DATE,
    "HISTORIA": VARCHAR(1),
    "CONTROLE": VARCHAR(1),
    "MANIPULA": VARCHAR(1),
    "MAECHAGA": VARCHAR(1),
    "ORAL": VARCHAR(1),
    "ASSINTOMA": VARCHAR(1),
    "EDEMA": VARCHAR(1),
    "MENINGOE": VARCHAR(1),
    "POLIADENO": VARCHAR(1),
    "FEBRE": VARCHAR(1),
    "HEPATOME": VARCHAR(1),
    "SINAIS_ICC": VARCHAR(1),
    "ARRITMIAS": VARCHAR(1),
    "ASTENIA": VARCHAR(1),
    "ESPLENOM": VARCHAR(1),
    "CHAGOMA": VARCHAR(1),
    "OUTRO_SIN": VARCHAR(1),
    "OUTRO_ESP": VARCHAR(30),
    "DT_COL_DIR": DATE,
    "EXAME": VARCHAR(1),
    "MICRO_HEMA": VARCHAR(1),
    "OUTRO": VARCHAR(1),
    "DT_COL_IND": DATE,
    "XENODIAG": VARCHAR(1),
    "HEMOCULT": VARCHAR(1),
    "DT_COL_S1": DATE,
    "DT_COL_S2": DATE,
    "ELI_IGM_S1": VARCHAR(1),
    "ELI_IGG_S1": VARCHAR(1),
    "ELI_IGM_S2": VARCHAR(1),
    "ELI_IGG_S2": VARCHAR(1),
    "HEM_IGM_S1": VARCHAR(1),
    "HEM_IGG_S1": VARCHAR(1),
    "HEM_IGM_S2": VARCHAR(1),
    "HEM_IGG_S2": VARCHAR(1),
    "IMU_IGM_S1": VARCHAR(1),
    "TIT_IGM_S1": VARCHAR(5),
    "IMU_IGM_S2": VARCHAR(1),
    "TIT_IGM_S2": NUMERIC(5),
    "IMU_IGG_S1": VARCHAR(1),
    "TIT_IGG_S1": NUMERIC(5),
    "IMU_IGG_S2": VARCHAR(1),
    "TIT_IGG_S2": NUMERIC(5),
    "RESUL_HIS": DATE,
    "RES_HIST": VARCHAR(1),
    "ESPECIFICO": VARCHAR(1),
    "SINTOMATIC": VARCHAR(1),
    "DROGA": VARCHAR(1),
    "TEMPO": NUMERIC(3),
    "CON_TRIAT": VARCHAR(1),
    "BIOSSEG": VARCHAR(1),
    "FISCALIZA": VARCHAR(1),
    "MED_OUTRO": VARCHAR(1),
    "OUTRO_DES": VARCHAR(30),
    "CLASSI_FIN": VARCHAR(1),
    "CRITERIO": VARCHAR(2),
    "CON_PROVAV": VARCHAR(1),
    "CON_OUTRA": VARCHAR(30),
    "CON_LOCAL": VARCHAR(1),
    "TPAUTOCTO": VARCHAR(1),
    "COUFINF": VARCHAR(2),
    "COPAISINF": VARCHAR(4),
    "COMUNINF": VARCHAR(6),
    "CODISINF": VARCHAR(4),
    "CO_BAINFC": NUMERIC(8),
    "NOBAIINF": VARCHAR(60),
    "DOENCA_TRA": VARCHAR(1),
    "DT_ENCERRA": DATE,
    "DS_OBS": VARCHAR(255),
    "EPIZOOTIAS": VARCHAR(1),
    "ISOL_VIR_N": VARCHAR(1),
    "VETOR_A": VARCHAR(1),
    "VACINADO": VARCHAR(1),
    "DT_VACINA": DATE,
    "UF_VAC": VARCHAR(2),
    "MUNCI_VAC": VARCHAR(6),
    "UNID_VAC": NUMERIC((8,0)),
    "DOR_ABDO_N": VARCHAR(1),
    "SINT_HEM_N": VARCHAR(1),
    "FAGET": VARCHAR(1),
    "EXCR_RENA_": VARCHAR(1),
    "HOSPITALIZ": VARCHAR(1),
    "DT_INTERNA": DATE,
    "UF": VARCHAR(2),
    "MUNICIPIO": VARCHAR(6),
    "HOSPITAL": VARCHAR(70),
    "BT": VARCHAR(6),
    "AST": NUMERIC(5),
    "BD": VARCHAR(6),
    "ALT": NUMERIC(5),
    "DT_COL_1": DATE,
    "S1_IGM": VARCHAR(1),
    "DT_COL_2": DATE,
    "S2_IGM": VARCHAR(1),
    "MAT_COLETA": VARCHAR(1),
    "DT_COLETA": DATE,
    "RES_ISOLAM": VARCHAR(1),
    "HISTOPA": VARCHAR(1),
    "IMUNOH": VARCHAR(1),
    "DT_PTPCR": DATE,
    "RES_PTPCR": VARCHAR(1),
    "CLASFIN_ES": VARCHAR(30),
    "LOCALIDADE": None,
    "CON_ATIVID": VARCHAR(1),
    "DTATEND": DATE,
    "NUATEND": NUMERIC((4,0)),
    "DTSUSPEIC": DATE,
    "STHOSPITAL": VARCHAR(1),
    "DTINTERNA": DATE,
    "DTALTA": DATE,
    "UF_HOSP": VARCHAR(2),
    "MUN_HOSP": VARCHAR(6),
    "UNID_HOSP": NUMERIC(7),
    "STFEBRE": VARCHAR(1),
    "STNAUSEA": VARCHAR(1),
    "STVOMITO": VARCHAR(1),
    "STDIARREIA": VARCHAR(1),
    "STCONSTIPA": VARCHAR(1),
    "STCEFALEIA": VARCHAR(1),
    "STTONTURA": VARCHAR(1),
    "STVISAO": VARCHAR(1),
    "STDIPLOPIA": VARCHAR(1),
    "STDISARTRI": VARCHAR(1),
    "STDISFONIA": VARCHAR(1),
    "STDISFAGIA": VARCHAR(1),
    "STBOCA": VARCHAR(1),
    "STFERIMENT": VARCHAR(1),
    "STFLACIDEZ": VARCHAR(1),
    "STDISPNEIA": VARCHAR(1),
    "STRESPIRA": VARCHAR(1),
    "STCARDIACA": VARCHAR(1),
    "STCOMA": VARCHAR(1),
    "STPARESTES": VARCHAR(1),
    "DS_PARES": VARCHAR(30),
    "STOUTROSIN": VARCHAR(1),
    "DS_OUTROSI": VARCHAR(30),
    "STPTOSE": VARCHAR(1),
    "STOFTALMO": VARCHAR(1),
    "STMIDRIASE": VARCHAR(1),
    "STFACIAL": VARCHAR(1),
    "STBULBAR": VARCHAR(1),
    "STMEMSUP": VARCHAR(1),
    "STMEMINF": VARCHAR(1),
    "STDESCENDE": VARCHAR(1),
    "STSIMETRIC": VARCHAR(1),
    "STSENSIVEL": VARCHAR(1),
    "TPNEURO": VARCHAR(1),
    "STALIMENTO": VARCHAR(1),
    "DSALIMENTO": VARCHAR(30),
    "STCOMERCIO": VARCHAR(1),
    "STCASEIRA": VARCHAR(1),
    "DS_INDUS": VARCHAR(30),
    "STEXPALIM": VARCHAR(1),
    "DS_INGEST": VARCHAR(4),
    "DS_INI_GES": VARCHAR(4),
    "DS_FIM_GES": VARCHAR(4),
    "STDOMICILI": VARCHAR(1),
    "STESCOLA": VARCHAR(1),
    "STTRABALHO": VARCHAR(1),
    "STRESTAURA": VARCHAR(1),
    "STFESTA": VARCHAR(1),
    "STOUTROLOC": VARCHAR(1),
    "DS_OUTR_LO": VARCHAR(30),
    "UF_ING": VARCHAR(2),
    "MUN_ING": VARCHAR(6),
    "NUCONSOME": NUMERIC(4),
    "STVENTILA": VARCHAR(1),
    "STANTIBIO": VARCHAR(1),
    "STSORO": VARCHAR(1),
    "STOUTROTRA": VARCHAR(1),
    "DS_TRAT": VARCHAR(30),
    "DTSORO": DATE,
    "STANTIBOTU": VARCHAR(1),
    "STSOROMAT": VARCHAR(1),
    "DTSOROCOL": DATE,
    "STSORORES": VARCHAR(1),
    "TPSOROTOX": VARCHAR(1),
    "STFEZESMAT": VARCHAR(1),
    "DTFEZESCOL": DATE,
    "STFEZESRES": VARCHAR(1),
    "TPFEZESTOX": VARCHAR(1),
    "DS_ALI1OUT": VARCHAR(30),
    "ST_ALI1COL": VARCHAR(1),
    "DT_ALI1COL": DATE,
    "RESALIM1": VARCHAR(1),
    "TP_ALI1TOX": VARCHAR(1),
    "DS_ALI2OUT": VARCHAR(30),
    "ST_ALI2COL": VARCHAR(1),
    "DT_ALI2COL": DATE,
    "RESALIM2": VARCHAR(1),
    "TP_ALI2TO": VARCHAR(1),
    "DS_OUTRO": VARCHAR(30),
    "TP_COLOUT": VARCHAR(1),
    "DT_COLOUT": DATE,
    "RESALIMOUT": VARCHAR(1),
    "TP_TOXOUTR": VARCHAR(1),
    "TP_LIQUOR": VARCHAR(1),
    "DT_LIQUOR": DATE,
    "NU_CELULA": VARCHAR(5),
    "NU_PROTEI": VARCHAR(5),
    "STELETRO": VARCHAR(1),
    "DTELETRO": DATE,
    "TP_SENSITI": VARCHAR(1),
    "TP_MOTORA": VARCHAR(1),
    "TP_REPETE": VARCHAR(1),
    "AGENTE_OUT": VARCHAR(30),
    "TPBOTULISM": VARCHAR(1),
    "STCLINICA": VARCHAR(1),
    "STBROMATO": VARCHAR(1),
    "TPCLINICA": VARCHAR(1),
    "TPBROMATO": VARCHAR(1),
    "DSCAUSALIM": VARCHAR(30),
    "DS_ALI1": VARCHAR(30),
    "DS_ALI2": VARCHAR(30),
    "DS_LOCAL1": VARCHAR(30),
    "DS_LOCAL2": VARCHAR(30),
    "AT_ATIVIDA": VARCHAR(2),
    "AT_LAMINA": VARCHAR(1),
    "AT_SINTOMA": VARCHAR(1),
    "DEXAME": DATE,
    "RESULT": VARCHAR(2),
    "PMM": NUMERIC(8),
    "PCRUZ": VARCHAR(1),
    "DSTRAESQUE": VARCHAR(30),
    "DTRATA": DATE,
    "LOC_INF": VARCHAR(60),
    "NU_LOTE_I": VARCHAR(7),
    "CEFALEIA": VARCHAR(1),
    "ABDOMINAL": VARCHAR(1),
    "MIALGIA": VARCHAR(1),
    "NAUSEA": VARCHAR(1),
    "EXANTEMA": VARCHAR(1),
    "DIARREIA": VARCHAR(1),
    "ICTERICIA": VARCHAR(1),
    "HIPEREMIA": VARCHAR(1),
    "PETEQUIAS": VARCHAR(1),
    "HEMORRAG": VARCHAR(1),
    "LINFADENO": VARCHAR(1),
    "CONVULSAO": VARCHAR(1),
    "NECROSE": VARCHAR(1),
    "PROSTACAO": VARCHAR(1),
    "CHOQUE": VARCHAR(1),
    "COMA": VARCHAR(1),
    "HEMORRAGI": VARCHAR(1),
    "RESPIRATO": VARCHAR(1),
    "OLIGURIA": VARCHAR(1),
    "OUTROS": VARCHAR(1),
    "CARRAPATO": VARCHAR(1),
    "CAPIVARA": VARCHAR(1),
    "CAO_GATO": VARCHAR(1),
    "BOVINO": VARCHAR(1),
    "EQUINOS": VARCHAR(1),
    "OUTROANI": VARCHAR(1),
    "ANIM_ESP": VARCHAR(30),
    "FOI_MATA": VARCHAR(1),
    "COUFHOSP": VARCHAR(2),
    "COMUNHOSP": VARCHAR(6),
    "COUNIHOSP": NUMERIC(7),
    "DIAGNO_LAB": VARCHAR(1),
    "DTS1": DATE,
    "DTS2": DATE,
    "IGM_S1": VARCHAR(1),
    "IGG_S1": VARCHAR(1),
    "IGM_S2": VARCHAR(1),
    "IGG_S2": VARCHAR(1),
    "ISOLAMENTO": VARCHAR(1),
    "AGENTE": VARCHAR(30),
    "HISTOPATO": VARCHAR(1),
    "IMUNOHIST": VARCHAR(1),
    "DIAG_DESCA": VARCHAR(30),
    "ZONA": VARCHAR(1),
    "AMBIENTE": VARCHAR(1),
    "ANT_TIPOCO": VARCHAR(1),
    "ANT_OUTROS": VARCHAR(30),
    "ANT_NOMECO": VARCHAR(70),
    "ANT_ENDECO": VARCHAR(60),
    "ANT_DOS_N": VARCHAR(1),
    "ANT_ULTI_D": DATE,
    "CLI_EDEMAG": VARCHAR(1),
    "CLI_PESCOC": VARCHAR(1),
    "CLI_FEBRE": VARCHAR(1),
    "CLI_PROSTR": VARCHAR(1),
    "CLI_PSEUDO": VARCHAR(1),
    "CLI_PALIDE": VARCHAR(1),
    "CLI_TEMPER": NUMERIC(3),
    "CLI_CAVIDA": VARCHAR(1),
    "CLI_AMIGDA": VARCHAR(1),
    "CLI_CORDAO": VARCHAR(1),
    "CLI_FARING": VARCHAR(1),
    "CLI_LARING": VARCHAR(1),
    "CLI_ORGAOS": VARCHAR(1),
    "CLI_PALATO": VARCHAR(1),
    "CLI_CONDUT": VARCHAR(1),
    "CLI_TRAQUE": VARCHAR(1),
    "CLI_PELE": VARCHAR(1),
    "CLI_CONJUN": VARCHAR(1),
    "CLI_MIOCAR": VARCHAR(1),
    "CLI_NEFRIT": VARCHAR(1),
    "CLI_PARALB": VARCHAR(1),
    "CLI_PARALP": VARCHAR(1),
    "CLI_ARRITM": VARCHAR(1),
    "CLI_PARALM": VARCHAR(1),
    "CLI_OUTRAS": VARCHAR(1),
    "CLI_ESPECI": VARCHAR(30),
    "ATE_HOSPIT": VARCHAR(1),
    "ATE_INTERN": DATE,
    "ATE_UF_INT": VARCHAR(2),
    "ATE_MUNICI": VARCHAR(6),
    "ATE_HOSP_1": NUMERIC((8,0)),
    "LAB_MATE_N": VARCHAR(1),
    "LAB_DATA_C": DATE,
    "LAB_CULTUR": VARCHAR(1),
    "LAB_PROVAS": VARCHAR(1),
    "TRA_DATA_S": DATE,
    "TRA_ANTIBI": VARCHAR(1),
    "TRA_DATA_A": DATE,
    "MED_IDEN_C": VARCHAR(1),
    "MED_QUAN_C": NUMERIC(3),
    "MED_CASO_S": VARCHAR(1),
    "MED_MATERI": VARCHAR(1),
    "MED_QUAN_M": NUMERIC(3),
    "MED_QUAN_P": NUMERIC(3),
    "MED_PREVEN": VARCHAR(1),
    "ID_AGRAVO": VARCHAR(1),
    "VOMITO": VARCHAR(1),
    "DOR_COSTAS": VARCHAR(1),
    "CONJUNTVIT": VARCHAR(1),
    "ARTRITE": VARCHAR(1),
    "ARTRALGIA": VARCHAR(1),
    "PETÉQUIA_N": VARCHAR(1),
    "LEUCOPENIA": VARCHAR(1),
    "LACO": VARCHAR(1),
    "DOR_RETRO": VARCHAR(1),
    "DIABETES": VARCHAR(1),
    "HEMATOLOG": VARCHAR(1),
    "HEPATOPAT": VARCHAR(1),
    "RENAL": VARCHAR(1),
    "HIPERTENSA": VARCHAR(1),
    "ÁCIDO_PEPT": VARCHAR(1),
    "AUTO_IMUNE": VARCHAR(1),
    "DT_CHIK_S1": DATE,
    "DT_CHIK_S2": DATE,
    "DT_PRNT": DATE,
    "RES_CHIKS1": VARCHAR(1),
    "RES_CHIKS2": VARCHAR(1),
    "RESUL_PRNT": VARCHAR(1),
    "DT_SORO": DATE,
    "RESUL_SORO": VARCHAR(1),
    "DT_NS1": DATE,
    "RESUL_NS1": VARCHAR(1),
    "DT_VIRAL": DATE,
    "RESUL_VI_N": VARCHAR(1),
    "DT_PCR": DATE,
    "RESUL_PCR_": VARCHAR(1),
    "SOROTIPO": VARCHAR(1),
    "HISTOPA_N": VARCHAR(1),
    "IMUNOH_N": VARCHAR(1),
    "DDD_HOSP": VARCHAR(2),
    "TEL_HOSP": VARCHAR(9),
    "CLINIC_CHIK": VARCHAR(1),
    "ALRM_HIPOT": VARCHAR(1),
    "ALRM_PLAQ": VARCHAR(1),
    "ALRM_VOM": VARCHAR(1),
    "ALRM_ABDOM": VARCHAR(1),
    "ALRM_LETAR": VARCHAR(1),
    "ALRM_SANG": VARCHAR(1),
    "ALRM_HEMAT": VARCHAR(1),
    "ALRM_HEPAT": VARCHAR(1),
    "ALRM_LIQ": VARCHAR(1),
    "DT_ALRM": DATE,
    "GRAV_PULSO": VARCHAR(1),
    "GRAV_CONV": VARCHAR(1),
    "GRAV_ENCH": VARCHAR(1),
    "GRAV_INSUF": VARCHAR(1),
    "GRAV_TAQUI": VARCHAR(1),
    "GRAV_EXTRE": VARCHAR(1),
    "GRAV_HIPOT": VARCHAR(1),
    "GRAV_HEMAT": VARCHAR(1),
    "GRAV_MELEN": VARCHAR(1),
    "GRAV_METRO": VARCHAR(1),
    "GRAV_SANG": VARCHAR(1),
    "GRAV_AST": VARCHAR(1),
    "GRAV_MIOC": VARCHAR(1),
    "GRAV_CONSC": VARCHAR(1),
    "GRAV_ORGAO": None,
    "DT_GRAV": DATE,
    "ANT_SENTIN": VARCHAR(1),
    "FC_CONTATO": VARCHAR(1),
    "OUT_CONTAT": VARCHAR(30),
    "NM_CONTATO": VARCHAR(40),
    "END_CONTAT": VARCHAR(60),
    "CS_VAC_N": VARCHAR(1),
    "DT_ULT_DOS": DATE,
    "DT_CATARRA": DATE,
    "CS_TOSSE_E": VARCHAR(1),
    "CS_TOSSE_P": VARCHAR(1),
    "CS_CRISE": VARCHAR(1),
    "CS_CIANOSE": VARCHAR(1),
    "CS_VOMITOS": VARCHAR(1),
    "CS_APNEIA": VARCHAR(1),
    "CS_TEMP37": VARCHAR(1),
    "CS_TEMP_38": VARCHAR(1),
    "CS_OUT_SIN": VARCHAR(1),
    "NM_OUT_SIN": VARCHAR(30),
    "CS_PNEUMON": VARCHAR(1),
    "CS_ENCEFAL": VARCHAR(1),
    "CS_DESITRA": VARCHAR(1),
    "CS_OTITE": VARCHAR(1),
    "CS_DESNUTR": VARCHAR(1),
    "CS_OUT_COM": VARCHAR(1),
    "NM_OUT_COM": VARCHAR(30),
    "CS_HOSPITA": VARCHAR(1),
    "COD_UF_HOS": VARCHAR(2),
    "COD_MUN_HO": VARCHAR(6),
    "COD_HOSP": NUMERIC(8),
    "CS_ANTIBIO": VARCHAR(1),
    "DT_ADM_ANT": DATE,
    "CS_COLETA": VARCHAR(1),
    "CS_CULTURA": VARCHAR(1),
    "COLET_COMU": VARCHAR(1),
    "QUAN_COMUN": NUMERIC(3),
    "QUAN_POSIT": NUMERIC(3),
    "MED_BLOQUE": VARCHAR(1),
    "HEPATITE_N": VARCHAR(1),
    "HEPATITA": VARCHAR(1),
    "HEPATITB": VARCHAR(1),
    "INSTITUCIO": VARCHAR(1),
    "HIV": VARCHAR(1),
    "OUTRA_DST": VARCHAR(1),
    "SEXUAL": VARCHAR(1),
    "DOMICILI": VARCHAR(1),
    "OCUPACIO": VARCHAR(1),
    "MEDICAMENT": VARCHAR(1),
    "TATU_PIER": VARCHAR(1),
    "MATBIOLOGI": VARCHAR(1),
    "INAL_CRACK": VARCHAR(1),
    "ACUPUNTURA": VARCHAR(1),
    "TRANSFUSAO": VARCHAR(1),
    "INJETAVEIS": VARCHAR(1),
    "CIRURGICO": VARCHAR(1),
    "AGUA_ALIME": VARCHAR(1),
    "DENTARIO": VARCHAR(1),
    "TRESMAIS": VARCHAR(1),
    "HEMODIALIS": VARCHAR(1),
    "TRANSPLA": VARCHAR(1),
    "OUTRAS": VARCHAR(1),
    "DT_ACIDENT": DATE,
    "CO_UF_EXP": VARCHAR(2),
    "CO_MUN_EXP": VARCHAR(6),
    "DS_LOC_EXP": VARCHAR(70),
    "NU_TEL_EXP": VARCHAR(9),
    "CO_UF_EX2": VARCHAR(2),
    "CO_MUN_EX2": VARCHAR(6),
    "DS_LOC_EX2": VARCHAR(70),
    "NU_TEL_EX2": VARCHAR(9),
    "CO_UF_EX3": VARCHAR(2),
    "CO_MUN_EX3": VARCHAR(6),
    "DS_LOC_EX3": VARCHAR(70),
    "NU_TEL_EX3": VARCHAR(9),
    "BANCOSANGU": VARCHAR(1),
    "RES_HBSAG": VARCHAR(1),
    "RE_ANTIHBC": VARCHAR(1),
    "RE_ANTIHCV": VARCHAR(1),
    "COLETAMARC": DATE,
    "ANTIHAVIGM": VARCHAR(1),
    "ANTIHBS": VARCHAR(1),
    "ANTIHDVIGM": VARCHAR(1),
    "AGHBS": VARCHAR(1),
    "AGHBE": VARCHAR(1),
    "ANTIHEVIGM": VARCHAR(1),
    "ANTIHBCIGM": VARCHAR(1),
    "ANTIHBE": VARCHAR(1),
    "ANTIHCV": VARCHAR(1),
    "HBC_TOTAL": VARCHAR(1),
    "ANTIHDV": VARCHAR(1),
    "TP_SOROHCV": VARCHAR(1),
    "GEN_VHC": VARCHAR(1),
    "FORMA": VARCHAR(1),
    "CLAS_ETIOL": VARCHAR(2),
    "FONTE": VARCHAR(2),
    "DSFONTE": VARCHAR(30),
    "ANT_CB_LAM": VARCHAR(1),
    "ANT_CB_CRI": VARCHAR(1),
    "ANT_CB_CAI": VARCHAR(1),
    "ANT_CB_FOS": VARCHAR(1),
    "ANT_CB_SIN": VARCHAR(1),
    "ANT_CB_PLA": VARCHAR(1),
    "ANT_CB_COR": VARCHAR(1),
    "ANT_CB_ROE": VARCHAR(1),
    "ANT_CB_GRA": VARCHAR(1),
    "ANT_CB_TER": VARCHAR(1),
    "ANT_CB_LIX": VARCHAR(1),
    "ANT_CB_OUT": VARCHAR(1),
    "ANT_OU_DES": VARCHAR(30),
    "ANT_HUMANO": VARCHAR(1),
    "ANT_ANIMAI": VARCHAR(1),
    "CLI_DT_ATE": DATE,
    "CLI_MIALGI": VARCHAR(1),
    "CLI_CEFALE": VARCHAR(1),
    "CLI_PROST": VARCHAR(1),
    "CLI_CONGES": VARCHAR(1),
    "CLI_PANTUR": VARCHAR(1),
    "CLI_VOMITO": VARCHAR(1),
    "CLI_DIARRE": VARCHAR(1),
    "CLI_ICTERI": VARCHAR(1),
    "CLI_RENAL": VARCHAR(1),
    "CLI_RESPIR": VARCHAR(1),
    "CLI_CARDIA": VARCHAR(1),
    "CLI_HEMOPU": VARCHAR(1),
    "CLI_HEMORR": VARCHAR(1),
    "CLI_MENING": VARCHAR(1),
    "CLI_OUTROS": VARCHAR(1),
    "CLI_OTRDES": VARCHAR(30),
    "ATE_HOSP": VARCHAR(1),
    "ATE_DT_INT": DATE,
    "ATE_DT_ALT": DATE,
    "ATE_UF": VARCHAR(2),
    "LAB_DT_1": DATE,
    "LAB_ELIS_1": VARCHAR(1),
    "LAB_DT_2": DATE,
    "LAB_ELIS_2": VARCHAR(1),
    "DTMICRO1": DATE,
    "MICRO1_S1": VARCHAR(5),
    "MICRO1_T_1": VARCHAR(4),
    "MICRO1_S_2": VARCHAR(5),
    "MICRO1_T_2": VARCHAR(5),
    "LAB_MICR_1": VARCHAR(1),
    "DTMICRO2": DATE,
    "MICRO2_S1": VARCHAR(5),
    "MICRO2_T_1": VARCHAR(4),
    "MICRO2_S_2": VARCHAR(5),
    "MICRO2_T_2": VARCHAR(4),
    "LAB_MICR_2": VARCHAR(1),
    "DTISOLA": DATE,
    "RES_ISOL": VARCHAR(1),
    "DTIMUNO": DATE,
    "RES_IMUNO": VARCHAR(1),
    "RES_PCR": VARCHAR(1),
    "CON_AREA": VARCHAR(1),
    "CON_AMBIEN": VARCHAR(1),
    "DT_RISCO1": DATE,
    "DT_RISCO2": DATE,
    "DT_RISCO3": DATE,
    "DT_RISCO4": DATE,
    "CO_MUN_R1": VARCHAR(6),
    "CO_MUN_R2": VARCHAR(6),
    "CO_MUN_R3": VARCHAR(6),
    "CO_MUN_R4": VARCHAR(6),
    "CO_UF_R1": VARCHAR(2),
    "CO_UF_R2": VARCHAR(2),
    "CO_UF_R3": VARCHAR(2),
    "CO_UF_R4": VARCHAR(2),
    "NO_END_R1": VARCHAR(60),
    "NO_END_R2": VARCHAR(60),
    "NO_END_R3": VARCHAR(60),
    "NO_END_R4": VARCHAR(60),
    "NO_LOC_R1": VARCHAR(60),
    "NO_LOC_R2": VARCHAR(60),
    "NO_LOC_R3": VARCHAR(60),
    "NO_LOC_R4": VARCHAR(60),
    "DT_COPRO": DATE,
    "AN_QUANT": NUMERIC(4),
    "AN_QUALI": VARCHAR(1),
    "OUTRO_EX": VARCHAR(40),
    "TRATAM": VARCHAR(1),
    "DTTRAT": DATE,
    "TRATANAO": VARCHAR(1),
    "STCURA1": VARCHAR(1),
    "STCURA2": VARCHAR(1),
    "STCURA3": VARCHAR(1),
    "DT_RESU3": DATE,
    "DS_FORMA": VARCHAR(30),
    "NOPROPIN": VARCHAR(100),
    "NOCOLINF": VARCHAR(100),
    "FRAQUEZA": VARCHAR(1),
    "EMAGRA": VARCHAR(1),
    "TOSSE": VARCHAR(1),
    "PALIDEZ": VARCHAR(1),
    "BACO": VARCHAR(1),
    "INFECCIOSO": VARCHAR(1),
    "FEN_HEMORR": VARCHAR(1),
    "FIGADO": VARCHAR(1),
    "OUTROS_ESP": VARCHAR(30),
    "DIAG_PAR_N": VARCHAR(1),
    "IFI": VARCHAR(1),
    "ENTRADA": VARCHAR(1),
    "TRATAMENTO": VARCHAR(1),
    "PESO": NUMERIC(3),
    "DOSE": VARCHAR(1),
    "AMPOLAS": NUMERIC(3),
    "FALENCIA": VARCHAR(1),
    "DT_DESLC1": DATE,
    "DS_MUN_1": VARCHAR(60),
    "CO_UF_1": VARCHAR(2),
    "CO_PAIS_1": NUMERIC(3),
    "DS_TRANS_1": VARCHAR(30),
    "DT_DESLC2": DATE,
    "DS_MUN_2": VARCHAR(60),
    "CO_UF_2": VARCHAR(2),
    "CO_PAIS_2": NUMERIC(3),
    "DS_TRANS_2": VARCHAR(30),
    "DT_DESLC3": DATE,
    "DS_MUN_3": VARCHAR(60),
    "CO_UF_3": VARCHAR(2),
    "CO_PAIS_3": NUMERIC(3),
    "DS_TRANS_3": VARCHAR(30),
    "TP_CAUSA": VARCHAR(1),
    "TP_CAUSOUT": VARCHAR(30),
    "TP_LOCALLE": VARCHAR(1),
    "NU_DOSE": VARCHAR(1),
    "TP_PROFILA": VARCHAR(1),
    "CS_TRISMO": VARCHAR(1),
    "CS_RISO": VARCHAR(1),
    "CS_OPISTOT": VARCHAR(1),
    "CS_NUCA": VARCHAR(1),
    "CS_ABDOMIN": VARCHAR(1),
    "CS_MEMBROS": VARCHAR(1),
    "CS_CRISES": VARCHAR(1),
    "CS_SIN_OUT": VARCHAR(1),
    "NM_SIN_OUT": VARCHAR(30),
    "TP_ORIGEM": VARCHAR(1),
    "SG_UF_INTE": VARCHAR(2),
    "NM_MUNIC_H": VARCHAR(6),
    "TP_IDENTFI": VARCHAR(1),
    "TP_VACINA": VARCHAR(1),
    "TP_ANALISE": VARCHAR(1),
    "CS_LOCAL": VARCHAR(1),
    "FC_CONT_DE": VARCHAR(30),
    "DDD": VARCHAR(2),
    "TEL_CONTAT": VARCHAR(9),
    "VINCULO": VARCHAR(1),
    "OUT_VINCUL": VARCHAR(30),
    "CS_ASSINTO": VARCHAR(1),
    "CS_DIARRE": VARCHAR(1),
    "CS_CAIMBRA": VARCHAR(1),
    "CS_FEBRE": VARCHAR(1),
    "CS_DOR": VARCHAR(1),
    "CS_CHOQUE": VARCHAR(1),
    "CS_DESIT": VARCHAR(1),
    "TIP_DIARRE": VARCHAR(1),
    "CS_FREQUEN": VARCHAR(1),
    "CS_SANGUE": VARCHAR(1),
    "CS_MUCO": VARCHAR(1),
    "CS_TIPO": VARCHAR(1),
    "DT_ATENDIM": DATE,
    "UF_HOSPITA": VARCHAR(2),
    "NM_HOSPITA": VARCHAR(70),
    "CS_MATERIA": VARCHAR(1),
    "CS_VOMITO": VARCHAR(1),
    "CS_ANTIB": VARCHAR(1),
    "NM_ANTIBIO": VARCHAR(30),
    "CS_RESULTA": VARCHAR(1),
    "CS_POSITIV": VARCHAR(1),
    "CS_NEG_ESP": VARCHAR(30),
    "CS_REIDRAT": VARCHAR(1),
    "CS_ANTIB_T": VARCHAR(1),
    "ANTIB_DES": VARCHAR(30),
    "NUM_CON_N": VARCHAR(1),
    "CS_VACTETA": VARCHAR(1),
    "DT_1_DOSE": DATE,
    "DT_2_DOSE": DATE,
    "DT_3_DOSE": DATE,
    "DT_REFORCO": DATE,
    "IDADE_MAE": NUMERIC(3),
    "NU_GESTA": VARCHAR(1),
    "ESCOLMAE_N": VARCHAR(2),
    "CS_NASCIDO": VARCHAR(1),
    "NO_OUPARTO": VARCHAR(30),
    "CS_ATEND_N": VARCHAR(1),
    "NO_ATENOUT": VARCHAR(30),
    "CS_SUGOU": VARCHAR(1),
    "CS_MAMAR": VARCHAR(1),
    "CS_CHORO": VARCHAR(1),
    "CS_ABDOMEN": VARCHAR(1),
    "CS_INF_COT": VARCHAR(1),
    "CS_OUTROS": VARCHAR(1),
    "DT_TRISMO": DATE,
    "CS_ORIGEM": VARCHAR(1),
    "CS_COBERTU": VARCHAR(1),
    "NO_COBOUTR": VARCHAR(30),
    "CS_VACINAC": VARCHAR(1),
    "CS_CADASTR": VARCHAR(1),
    "CS_DIVULGA": VARCHAR(1),
    "CS_BUSCAAT": VARCHAR(1),
    "CS_ORIENTA": VARCHAR(1),
    "CS_ANALISE": VARCHAR(1),
    "CS_OUTRAS": VARCHAR(1),
    "NO_OUTRAS": VARCHAR(30),
    "DS_INF_LOC": VARCHAR(1),
    "DS_INF_OUT": VARCHAR(30),
    "COUNIDINF": VARCHAR(7),
    "SIT_TRAB": VARCHAR(2),
    "TRAB_DESC": VARCHAR(30),
    "LOC_EXPO": VARCHAR(1),
    "LOC_EXP_DE": VARCHAR(30),
    "NOEMPRESA": VARCHAR(70),
    "CNAE": VARCHAR(10),
    "UF_EMP": VARCHAR(2),
    "MUN_EMP": VARCHAR(6),
    "DIS_EMP": VARCHAR(9),
    "COBAIEMP": VARCHAR(8),
    "NOBAIEMP": VARCHAR(60),
    "END_EMP": VARCHAR(60),
    "NU_EMP": VARCHAR(6),
    "COMP_EMP": VARCHAR(60),
    "REF_EMP": VARCHAR(60),
    "CEP_EMP": VARCHAR(7),
    "DDD_EMP": VARCHAR(3),
    "FONE_EMP": VARCHAR(9),
    "ZONA_EXP": VARCHAR(1),
    "PAIS_EXP": VARCHAR(4),
    "AGENTE_TOX": VARCHAR(2),
    "OUT_AGENTE": VARCHAR(30),
    "COAGTOXMA1": NUMERIC(3),
    "AGENTE_1": VARCHAR(60),
    "P_ATIVO_1": VARCHAR(60),
    "COAGTOXMA2": NUMERIC(3),
    "AGENTE_2": VARCHAR(60),
    "P_ATIVO_2": VARCHAR(60),
    "COAGTOXMA3": NUMERIC(3),
    "AGENTE_3": VARCHAR(60),
    "P_ATIVO_3": VARCHAR(60),
    "UTILIZACAO": VARCHAR(1),
    "UTIL_DESC": VARCHAR(30),
    "ATIVIDA_1": VARCHAR(2),
    "ATIVIDA_2": VARCHAR(2),
    "ATIVIDA_3": VARCHAR(2),
    "LAVOURA": VARCHAR(100),
    "VIA_1": VARCHAR(1),
    "VIA_2": VARCHAR(1),
    "VIA_3": VARCHAR(1),
    "CIRCUNSTAN": VARCHAR(2),
    "CIRCUN_DES": VARCHAR(30),
    "TPEXP": VARCHAR(1),
    "NUTEMPO": VARCHAR(2),
    "TPTEMPO": VARCHAR(1),
    "TPATENDE": VARCHAR(1),
    "CNES_HOSP": VARCHAR(8),
    "DIAG_CONF": VARCHAR(4),
    "CAT": VARCHAR(1),
    "TREINA_MIL": VARCHAR(1),
    "DESMATA_N": VARCHAR(1),
    "EXPO_N": VARCHAR(1),
    "MOAGEM_N": VARCHAR(1),
    "DORMIU_N": VARCHAR(1),
    "TRANSPO_N": VARCHAR(1),
    "PESCOU_N": VARCHAR(1),
    "ROEDOR_N": VARCHAR(1),
    "OUTRA_ATIV": VARCHAR(1),
    "OUTR_ATI_D": VARCHAR(40),
    "CLI_LOCAL": VARCHAR(30),
    "CLI_TOSSE": VARCHAR(1),
    "CLI_DISPNE": VARCHAR(1),
    "CLI_RESPI": VARCHAR(1),
    "CLI_MIAL_G": VARCHAR(1),
    "CLI_LOMBAR": VARCHAR(1),
    "CLI_ABDOMI": VARCHAR(1),
    "CLI_HIPOTE": VARCHAR(1),
    "CLI_CHOQUE": VARCHAR(1),
    "CLI_TORACI": VARCHAR(1),
    "CLI_TONTUR": VARCHAR(1),
    "CLI_NEUROL": VARCHAR(1),
    "CLI_ASTENI": VARCHAR(1),
    "CLI_PETEQU": VARCHAR(1),
    "CLI_HEMO": VARCHAR(1),
    "CLI_H_DESC": VARCHAR(30),
    "CLI_OUT_D": VARCHAR(30),
    "AM_SANGUE": VARCHAR(1),
    "LAB_HEMA_N": VARCHAR(1),
    "LAB_TROMBO": VARCHAR(1),
    "LAB_ATIPIC": VARCHAR(1),
    "LAB_UREIA": VARCHAR(1),
    "LAB_TGO": VARCHAR(1),
    "LAB_TGO_D": VARCHAR(30),
    "LAB_TGP": VARCHAR(1),
    "LAB_TGP_D": VARCHAR(30),
    "LAB_RES_B": VARCHAR(30),
    "LAB_RADIOL": VARCHAR(1),
    "LAB_DIFUSO": VARCHAR(1),
    "LAB_LOCAL": VARCHAR(1),
    "LAB_DERRAM": VARCHAR(1),
    "DT_COL_IGM": DATE,
    "LAB_IGM_R": VARCHAR(1),
    "LAB_IMUNO": VARCHAR(1),
    "LAB_RTPCR": VARCHAR(1),
    "TRA_HOSP": VARCHAR(1),
    "TRA_DT_INT": DATE,
    "TRA_UF": VARCHAR(2),
    "TRA_MUNICI": VARCHAR(6),
    "TRA_HOSPIT": NUMERIC((8,0)),
    "TRA_MECANI": VARCHAR(1),
    "TRA_ANTIVI": VARCHAR(1),
    "TRA_CORTIC": VARCHAR(1),
    "TRA_CPAP": VARCHAR(1),
    "TRA_VASOAT": VARCHAR(1),
    "TRA_TRATAM": VARCHAR(1),
    "TRA_ESPECI": VARCHAR(30),
    "CON_FORMA": VARCHAR(1),
    "ZONA_INFEC": VARCHAR(1),
    "CON_AMB_DE": VARCHAR(30),
    "CON_LOCALI": NUMERIC(2),
    "CON_LOCAL2": VARCHAR(1),
    "DT_EVOLUC": DATE,
    "CON_AUTOPS": VARCHAR(1),
    "NU_PRONTUA": VARCHAR(10),
    "POP_LIBER": VARCHAR(1),
    "POP_RUA": VARCHAR(1),
    "POP_SAUDE": VARCHAR(1),
    "POP_IMIG": VARCHAR(1),
    "BENEF_GOV": None,
    "EXTRAPU_N": VARCHAR(2),
    "EXTRAPUL_O": VARCHAR(30),
    "AGRAVAIDS": VARCHAR(1),
    "AGRAVALCOO": VARCHAR(1),
    "AGRAVDIABE": VARCHAR(1),
    "AGRAVDOENC": VARCHAR(1),
    "AGRAVDROGAS": VARCHAR(1),
    "AGRAVTABACO": VARCHAR(1),
    "AGRAVOUTRA": VARCHAR(1),
    "AGRAVOUTDE": VARCHAR(30),
    "BACILOSC_E": VARCHAR(1),
    "RAIOX_TORA": VARCHAR(1),
    "ANTIRRETROVIRAL": VARCHAR(1),
    "HISTOPATOL": VARCHAR(1),
    "CULTURA_ES": VARCHAR(1),
    "TESTE_MOLEC": VARCHAR(1),
    "TEST_SENSIBILID": None,
    "DT_INIC_TR": DATE,
    "NU_COMU_ID": NUMERIC(2),
    "SG_UF_ATUAL": None,
    "ID_MUNIC_AT": None,
    "NU_NOTI_AT": None,
    "DT_NOTI_AT": DATE,
    "ID_UNID_AT": VARCHAR(7),
    "SG_UF_2": None,
    "ID_MUNIC_2": None,
    "NU_CEP2": None,
    "D_DISTR_2": None,
    "ID_BAIRRO2 NM_BAIRRO2": None,
    "BACILOSC_1": None,
    "BACILOSC_2": None,
    "BACILOSC_3": None,
    "BACILOSC_4": None,
    "BACILOSC_5": None,
    "BACILOSC_6": None,
    "BACILOSC_APOS_6": None,
    "NU_PRONT_AT": None,
    "TRATSUP_AT": None,
    "NU_CONT_EX": None,
    "SITUA_ENCE": None,
    "TRANSF": None,
    "SG_UF_TRANSF": None,
    "MUN_TRANSF": None,
    "DT_ENCERRA  ": None,
    "OPORTU": None,
    "DT_OPORTU": None,
    "CONTATO": VARCHAR(1),
    "CONT_OUT": VARCHAR(30),
    "NM_CONTAT": VARCHAR(70),
    "DDD": VARCHAR(2),
    "TEL_CONTAT": VARCHAR(9),
    "SUGE_VINCU": VARCHAR(1),
    "VINC_OUT": VARCHAR(30),
    "ASSINTOMAT": VARCHAR(1),
    "CONSTIPA": VARCHAR(1),
    "ESPLENO": VARCHAR(1),
    "TIFICA": VARCHAR(1),
    "NAUSEAS": VARCHAR(1),
    "VOMITOS": VARCHAR(1),
    "DOR": VARCHAR(1),
    "PULSO": VARCHAR(1),
    "ENTERO": VARCHAR(1),
    "PERFURA": VARCHAR(1),
    "COMP_OUT": VARCHAR(1),
    "COMP_OUT_D": VARCHAR(30),
    "ATENDIMENT": VARCHAR(1),
    "DT_ATENDE": DATE,
    "SANGUE": VARCHAR(1),
    "FEZES": VARCHAR(1),
    "URINA": VARCHAR(1),
    "ANTIBIOTIC": VARCHAR(1),
    "DT_HEMO1": DATE,
    "HEMO_R1": VARCHAR(1),
    "HEMO_D_1": VARCHAR(30),
    "DT_HEMO2": DATE,
    "HEMO_R2": VARCHAR(1),
    "HEMO_D_2": VARCHAR(30),
    "DT_HEMO3": DATE,
    "HEMO_R3": VARCHAR(1),
    "HEMO_D_3": VARCHAR(30),
    "DT_URO": DATE,
    "URO_R1": VARCHAR(1),
    "URO_D": VARCHAR(30),
    "DT_URO2": DATE,
    "URO_R2": VARCHAR(1),
    "URO_D_2": VARCHAR(30),
    "DT_URO3": DATE,
    "URO_R3": VARCHAR(1),
    "URO_D_3": VARCHAR(30),
    "DT_COPRO1": DATE,
    "COPRO_R1": VARCHAR(1),
    "COPRO_D_1": VARCHAR(30),
    "DT_COPRO2": DATE,
    "COPRO_R2": VARCHAR(1),
    "COPRO_D_2": VARCHAR(30),
    "DT_COPRO3": DATE,
    "COPRO_R3": VARCHAR(1),
    "COPRO_D_3": VARCHAR(30),
    "DT_OUTR1": DATE,
    "OUTR_R1": VARCHAR(1),
    "OUTR_D1": VARCHAR(30),
    "DT_OUTR2": DATE,
    "OUTR_R2": VARCHAR(1),
    "OUTR_D2": VARCHAR(30),
    "DT_OUTR3": DATE,
    "OUTR_R3": VARCHAR(1),
    "OUTR_D3": VARCHAR(30),
    "CLORAFEN": VARCHAR(1),
    "AMPICILINA": VARCHAR(1),
    "SULFA": VARCHAR(1),
    "QUINOLONA": VARCHAR(1),
    "ANT_OUTR": VARCHAR(1),
    "ANT_OUT_D": VARCHAR(30),
    "DIAS": VARCHAR(2),
    "ANT_DT_ACI": DATE,
    "ANT_UF": VARCHAR(2),
    "ANT_MUNIC_": VARCHAR(6),
    "ANT_LOCALI": VARCHAR(60),
    "ANT_ZONA": VARCHAR(1),
    "ANT_TEMPO_": VARCHAR(1),
    "ANT_LOCA_1": VARCHAR(1),
    "MCLI_LOCAL": VARCHAR(1),
    "CLI_DOR": VARCHAR(1),
    "CLI_EDEMA": VARCHAR(1),
    "CLI_EQUIMO": VARCHAR(1),
    "CLI_NECROS": VARCHAR(1),
    "CLI_LOCAL_": VARCHAR(1),
    "CLI_LOCA_1": VARCHAR(30),
    "MCLI_SIST": VARCHAR(1),
    "CLI_NEURO": VARCHAR(1),
    "CLI_VAGAIS": VARCHAR(1),
    "CLI_MIOLIT": VARCHAR(1),
    "CLI_OUTR_2": VARCHAR(1),
    "CLI_OUTR_3": VARCHAR(30),
    "CLI_TEMPO_": VARCHAR(1),
    "TP_ACIDENT": VARCHAR(1),
    "ANI_TIPO_1": VARCHAR(30),
    "ANI_SERPEN": VARCHAR(1),
    "ANI_ARANHA": VARCHAR(1),
    "ANI_LAGART": VARCHAR(1),
    "TRA_CLASSI": VARCHAR(1),
    "CON_SOROTE": VARCHAR(1),
    "NU_AMPOLAS": NUMERIC(2),
    "NU_AMPOL_1": NUMERIC(2),
    "NU_AMPOL_8": NUMERIC(2),
    "NU_AMPOL_6": NUMERIC(2),
    "NU_AMPOL_4": NUMERIC(2),
    "NU_AMPOL_7": NUMERIC(2),
    "NU_AMPOL_5": NUMERIC(2),
    "NU_AMPOL_9": NUMERIC(2),
    "NU_AMPOL_3": NUMERIC(2),
    "COM_LOC": VARCHAR(1),
    "COM_SECUND": VARCHAR(1),
    "COM_NECROS": VARCHAR(1),
    "COM_COMPAR": VARCHAR(1),
    "COM_DEFICT": VARCHAR(1),
    "COM_APUTAC": VARCHAR(1),
    "COM_SISTEM": VARCHAR(1),
    "COM_RENAL": VARCHAR(1),
    "COM_EDEMA": VARCHAR(1),
    "COM_SEPTIC": VARCHAR(1),
    "COM_CHOQUE": VARCHAR(1),
    "CLI_CUTANE": VARCHAR(1),
    "CLI_MUCOSA": VARCHAR(1),
    "CLI_CICATR": VARCHAR(1),
    "CLI_CO_HIV": VARCHAR(1),
    "LAB_PARASI": VARCHAR(1),
    "LAB_IRM": VARCHAR(1),
    "LAB_HISTOP": VARCHAR(1),
    "CLA_TIPO_N": VARCHAR(1),
    "CLAS_FORMA": VARCHAR(1),
    "TRA_DROGA_": VARCHAR(1),
    "TRA_PESO": NUMERIC(3),
    "TRA_DOSE": VARCHAR(1),
    "TRA_AMPOLA": NUMERIC(3),
    "TRA_OUTR_N": VARCHAR(1),
    "CON_CLASS_": VARCHAR(1),
    "CO_RISCO": VARCHAR(1),
    "EPI_PESTE": VARCHAR(1),
    "COM_PEST": VARCHAR(1),
    "SIN_GANG": VARCHAR(1),
    "SIN_PULM": VARCHAR(1),
    "TB_INVESTIGA_PESTE": VARCHAR(1),
    "LAB_HEMO": VARCHAR(1),
    "LAB_ESFR": VARCHAR(1),
    "DT_S1": DATE,
    "DT_S2": DATE,
    "ELISA1": VARCHAR(1),
    "ELISA2": VARCHAR(1),
    "HEMO_IGM": VARCHAR(1),
    "IGM_T1": VARCHAR(2),
    "HEMO_IGG": VARCHAR(1),
    "IGG_T2": VARCHAR(5),
    "TRATADO": VARCHAR(1),
    "CO_FOCAL": VARCHAR(1),
    "CON_CLASSI": VARCHAR(1),
    "CON_GRAVID": VARCHAR(1),
    "NU_LESOES": NUMERIC(2),
    "FORMACLINI": VARCHAR(1),
    "CLASSOPERA": VARCHAR(1),
    "NERVOSAFET": NUMERIC(2),
    "AVALIA_N": VARCHAR(1),
    "MODOENTR": VARCHAR(1),
    "MODODETECT": VARCHAR(1),
    "BACILOSCO": VARCHAR(1),
    "DTINICTRAT": DATE,
    "ESQ_INI_N": VARCHAR(1),
    "CONTREG": NUMERIC(2),
    "MIGRADO_W": VARCHAR(1),
    "UFATUAL": VARCHAR(2),
    "ID_MUNI_AT": VARCHAR(6),
    "NU_NOT_AT": VARCHAR(7),
    "UFRESAT": VARCHAR(2),
    "MUNIRESAT": VARCHAR(6),
    "CEP": VARCHAR(8),
    "DISTRIT_AT": VARCHAR(60),
    "BAIRROAT": NUMERIC(8),
    "NOBAIRROAT": VARCHAR(60),
    "DTULTCOMP": DATE,
    "CLASSATUAL": VARCHAR(1),
    "AVAL_ATU_N": VARCHAR(1),
    "ESQ_ATU_N": VARCHAR(1),
    "DOSE_RECEB": NUMERIC(2),
    "EPIS_RACIO": VARCHAR(1),
    "DTMUDESQ": DATE,
    "CONTEXAM": NUMERIC(2),
    "TPALTA_N": VARCHAR(1),
    "DTALTA_N": DATE,
    "IN_VINCULA": VARCHAR(1),
    "NU_LOTE_IA": VARCHAR(7),
    "PRE_MUNIRE": VARCHAR(6),
    "PRE_UNIPRE": NUMERIC((8,0)),
    "PRE_SISPRE": VARCHAR(10),
    "TPEVIDENCI": VARCHAR(1),
    "TPTESTE1": VARCHAR(1),
    "DSTITULO1": VARCHAR(30),
    "DTTESTE1": DATE,
    "TPCONFIRMA": VARCHAR(10),
    "TPESQUEMA": VARCHAR(1),
    "TRATPARC": VARCHAR(1),
    "TPESQPAR": VARCHAR(1),
    "TPMOTPARC": VARCHAR(1),
    "DSMOTIVO": VARCHAR(30),
    "ARRANHAO": VARCHAR(1),
    "LAMBEDURA": VARCHAR(1),
    "MORDEDURA": VARCHAR(1),
    "MUCOSA": VARCHAR(1),
    "CABECA": VARCHAR(1),
    "MAOS_N": VARCHAR(1),
    "PES": VARCHAR(1),
    "TRONCO": VARCHAR(1),
    "SUPERIORES": VARCHAR(1),
    "INFERIORES": VARCHAR(1),
    "FERIMENT_N": VARCHAR(1),
    "PROFUNDO": VARCHAR(1),
    "SUPERFICIA": VARCHAR(1),
    "DILACERANT": VARCHAR(1),
    "DT_EXPO": DATE,
    "ANTEC_PRE": VARCHAR(1),
    "ANTEC_POS": VARCHAR(1),
    "NUM_DOSES": NUMERIC(2),
    "DT_TR_RAB": DATE,
    "ESPECIE_N": VARCHAR(1),
    "ESP_OUT": VARCHAR(30),
    "VACINAD": VARCHAR(1),
    "AEROFOBIA": VARCHAR(1),
    "HIDROFOBI": VARCHAR(1),
    "DISFAGIA": VARCHAR(1),
    "PARESTESI": VARCHAR(1),
    "AGRESSIVI": VARCHAR(1),
    "PARALISIA": VARCHAR(1),
    "AGITACAO": VARCHAR(1),
    "ANTI_RAB": VARCHAR(1),
    "DT_R_TRA": DATE,
    "DOSES_A": NUMERIC(2),
    "DT_VAC1": DATE,
    "DT_VAC_ULT": DATE,
    "TRA_SORO": VARCHAR(1),
    "DT_APLI_SO": DATE,
    "QUANTID": NUMERIC(3),
    "INFILTRA": VARCHAR(1),
    "IMUNO_DIRE": VARCHAR(1),
    "PROVA_BIOL": VARCHAR(1),
    "IMUNO_INDI": VARCHAR(1),
    "HISTOLOG_N": VARCHAR(1),
    "VARIA_VIR": NUMERIC(2),
    "CON_ZONA": VARCHAR(1),
    "ANT_AC": VARCHAR(1),
    "ANT_DOSE_3": NUMERIC(2),
    "ANT_DTUL_3": DATE,
    "ANT_BC": VARCHAR(1),
    "ANT_DOSES_": NUMERIC(2),
    "ANT_DTULT_": DATE,
    "ANT_CONJ_C": VARCHAR(1),
    "ANT_DOSE_C": NUMERIC(2),
    "ANT_DTUL_C": DATE,
    "ANT_BCG": VARCHAR(1),
    "ANT_DOSE_4": NUMERIC(2),
    "ANT_DTUL_4": DATE,
    "ANT_TRIPLI": VARCHAR(1),
    "ANT_DOSE_5": NUMERIC(2),
    "ANT_DTUL_5": DATE,
    "ANT_HEMO_T": VARCHAR(1),
    "ANT_DOSE_T": NUMERIC(2),
    "ANT_DTUL_T": DATE,
    "ANT_PNEUMO": VARCHAR(1),
    "ANT_DOSE_7": NUMERIC(2),
    "ANT_DTUL_7": DATE,
    "ANT_OUTRA": VARCHAR(1),
    "ANT_OU_DE": VARCHAR(30),
    "ANT_DTUL_8": DATE,
    "ANT_AIDS": VARCHAR(1),
    "ANT_IMUNO": VARCHAR(1),
    "ANT_IRA": VARCHAR(1),
    "ANT_TUBE": VARCHAR(1),
    "ANT_TRAUMA": VARCHAR(1),
    "ANT_INF_HO": VARCHAR(1),
    "ANT_OUTRO": VARCHAR(1),
    "ANT_OUTR_D": VARCHAR(30),
    "A NT_CONT_N": VARCHAR(1),
    "ANT_TELECO": VARCHAR(9),
    "ANT_SECUND": VARCHAR(1),
    "CLI_CONVUL": VARCHAR(1),
    "CLI_RIGIDE": VARCHAR(1),
    "CLI_KERNIG": VARCHAR(1),
    "CLI_ABAULA": VARCHAR(1),
    "CLI_COMA": VARCHAR(1),
    "ATE_UF_HOS": VARCHAR(2),
    "LAB_PUNCAO": VARCHAR(1),
    "LAB_DTPUNC": DATE,
    "LAB_ASPECT": VARCHAR(1),
    "LAB_CTLIQU.": VARCHAR(2),
    "LAB_CTLESA": VARCHAR(2),
    "LAB_CTSANG": VARCHAR(2),
    "LAB_CTESCA": VARCHAR(2),
    "LAB_BCLIQU": VARCHAR(2),
    "LAB_BCLESA": VARCHAR(2),
    "LAB_BCSANG": VARCHAR(2),
    "LAB_BCESCA": VARCHAR(2),
    "LAB_CILIQU": VARCHAR(2),
    "LAB_CISANG": VARCHAR(2),
    "LAB_AGLIQU": VARCHAR(2),
    "LAB_AGSANG": VARCHAR(2),
    "LAB_ISLIQU": VARCHAR(2),
    "LAB_ISFEZE": VARCHAR(2),
    "LAB_PCLIQU": VARCHAR(2),
    "LAB_PCLESA": VARCHAR(2),
    "LAB_PCSANG": VARCHAR(2),
    "LAB_PCESCA": VARCHAR(2),
    "CON_DIAGES": VARCHAR(2),
    "CLA_ME_BAC": VARCHAR(4),
    "CLA_ME_ASS": VARCHAR(4),
    "CLA_ME_ETI": VARCHAR(4),
    "CLA_SOROGR": NUMERIC(4),
    "MED_NUCOMU": NUMERIC(2),
    "MED_QUIMIO": VARCHAR(1),
    "MED_DT_QUI": DATE,
    "MED_DT_EVO": DATE,
    "LAB_HEMA": NUMERIC(5),
    "LAB_NEUTRO": NUMERIC(3),
    "LAB_GLICO": NUMERIC(5),
    "LAB_LEUCO": NUMERIC(5),
    "LAB_EOSI": NUMERIC(3),
    "LAB_PROT": NUMERIC(5),
    "LAB_MONO": NUMERIC(3),
    "LAB_LINFO": NUMERIC(3),
    "LAB_CLOR": NUMERIC(5),
}
