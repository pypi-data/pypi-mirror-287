from rdkit import Chem, RDLogger
import pandas as pd
import sys
import os

class Sdf:
    def __init__(self):
        pass

    def process_sdf(self, input_file, database, batch_size, affinity_cutoff=None):
        if os.path.exists("sdf"):
            existing_files = [f for f in os.listdir("sdf") if f.startswith(database)]
            if existing_files:
                return print(f'\nThere are already {database} files in the folder.\n')
        else:
            os.makedirs("sdf")
        try:
            with open(input_file, 'r') as file:
                lines = file.readlines()
        except:
            return print('\nFILE NOT FOUND\n')

        current_molecule = []
        current_affinity = None
        first_database_name = None

        def save_batch(batch, index):
            with open(os.path.join("sdf", f"{database}_{index:04d}.sdf"), 'w') as f:
                f.writelines(batch)

        batch = []
        file_index = 1
        molecule_count = 0

        for i, line in enumerate(lines):
            if not current_molecule:
                first_database_name = line.split()[0] if line.strip() else None
                if first_database_name:
                    current_molecule.append(first_database_name + '\n')
            else:
                current_molecule.append(line)

            if line.startswith('>  <minimizedAffinity>'):
                current_affinity = float(lines[i + 1].strip())

            if line.strip() == '$$$$':
                if affinity_cutoff is None or (current_affinity is not None and current_affinity <= affinity_cutoff):
                    batch.extend(current_molecule)
                    molecule_count += 1

                current_molecule = []
                current_affinity = None
                first_database_name = None

                if molecule_count == batch_size:
                    save_batch(batch, file_index)
                    file_index += 1
                    batch = []
                    molecule_count = 0

        if batch:
            save_batch(batch, file_index)

        print(f"\nProcessing finished. \n{file_index} batch(es) saved in folder 'sdf'.\n")

class AdmetSpreadsheet:

    ''' Analyzes the AdmetLab 3.0 spreadsheet '''

    def __init__(self, input = None, weights=None):
        self.input = input
        self.df = None
        self.df_analysis = None
        self.weights = weights
        self.new_cols_to_move = ['SCORE', 'ABSORTION', 'DISTRIBUTION', 'TOXICITY', 'TOX21_PATHWAY', 'METABOLISM', 'TOXICOPHORE_RULES', 'EXCRETION', 'MEDICINAL_CHEMISTRY']
        self.weights = weights

    def replace_interval(self, valor, intervals, values):
        for interval, valor_substituido in zip(intervals, values):
            if interval[0] <= valor <= interval[1]:
                return valor_substituido
        return valor

    def replace_values(self, df, columns, intervals, values):
        replace = lambda x: self.replace_interval(pd.to_numeric(x, errors='coerce'), intervals, values)
        for col in columns:
            df[col] = df[col].apply(replace)
        return df

    def substituir_string(self, valor, string, valor1, valor2):
        return valor1 if valor == string else valor2
    
    def normalize_values(self, value):
        if value <= 1.0:
            return float(value * 1000)
        return float(value)
    
    def rename(self,df):
        df = df.rename(columns={
            'cl-plasma': 'cl_plasma',
            't0.5': 't_0_5',
            'MCE-18': 'MCE_18',
            })
        return df

    def process_data(self, df, weights):

        self.df = df

        self.weights = weights if weights is not None else {
            "ABSORTION": 2,
            "DISTRIBUTION": 1,
            "TOXICITY": 8,
            "TOX21_PATHWAY": 3,
            "METABOLISM": 2,
            "TOXICOPHORE_RULES": 3,
            "EXCRETION": 1,
            "MEDICINAL_CHEMISTRY": 5
        }

        self.df = self.rename(self.df)

        absorption_columns_float = ['PAMPA', 'pgp_inh', 'pgp_sub', 'hia', 'f20', 'f30', 'f50']
        absorption_columns_str = ['FAF-Drugs4 Rule']
        absorption_columns = absorption_columns_float + absorption_columns_str

        distribution_columns = ['OATP1B1', 'OATP1B3', 'BCRP', 'BSEP', 'BBB', 'MRP1']
        toxicity_columns = ['hERG', 'hERG-10um', 'DILI', 'Ames', 'ROA', 'FDAMDD', 'SkinSen', 'Carcinogenicity', 'EC', 'EI', 'Respiratory', 'H-HT', 'Neurotoxicity-DI', 'Ototoxicity', 'Hematotoxicity', 'Nephrotoxicity-DI', 'Genotoxicity', 'RPMI-8226', 'A549', 'HEK293']
        tox21_columns = ['NR-AhR', 'NR-AR', 'NR-AR-LBD', 'NR-Aromatase', 'NR-ER', 'NR-ER-LBD', 'NR-PPAR-gamma', 'SR-ARE', 'SR-ATAD5', 'SR-HSE', 'SR-MMP', 'SR-p53']
        metabolism_columns = ['CYP1A2-inh', 'CYP1A2-sub', 'CYP2C19-inh', 'CYP2C19-sub', 'CYP2C9-inh', 'CYP2C9-sub', 'CYP2D6-inh', 'CYP2D6-sub', 'CYP3A4-inh', 'CYP3A4-sub', 'CYP2B6-inh', 'CYP2B6-sub', 'CYP2C8-inh', 'LM-human']
        toxicophore_columns = ['NonBiodegradable', 'NonGenotoxic_Carcinogenicity', 'SureChEMBL', 'Skin_Sensitization', 'Acute_Aquatic_Toxicity', 'Genotoxic_Carcinogenicity_Mutagenicity']

        medicinal_chemistry_columns_str = ['Alarm_NMR', 'BMS', 'Chelating', 'PAINS']
        medicinal_chemistry_columns_float_divergent = ['gasa', 'QED', 'Synth', 'Fsp3', 'MCE_18', 'Lipinski', 'Pfizer', 'GSK', 'GoldenTriangle']
        medicinal_chemistry_columns_float_similar = ['Aggregators', 'Fluc', 'Blue_fluorescence', 'Green_fluorescence', 'Reactive', 'Promiscuous']
        medicinal_chemistry = medicinal_chemistry_columns_str + medicinal_chemistry_columns_float_divergent + medicinal_chemistry_columns_float_similar

        to_normalize = ['caco2','PPB', 'Fu','logVDss','cl_plasma', 't_0_5', 'QED', 'Synth', 'Fsp3', 'MCE_18']
        normalize = absorption_columns_float + distribution_columns + toxicity_columns + tox21_columns + metabolism_columns + medicinal_chemistry_columns_float_similar + to_normalize
        
        for coluna in normalize:
            self.df[coluna] = self.df[coluna].apply(self.normalize_values)

        self.df = self.replace_values(self.df, absorption_columns_float, [(0, 300), (300, 700), (700, 1000)], [1.1, 0.55, 0.0])
        self.df = self.replace_values(self.df, distribution_columns, [(0, 300), (300, 700), (700, 1000)], [1.1, 0.55, 0.0])
        self.df = self.replace_values(self.df, toxicity_columns, [(0, 300), (300, 700), (700, 1000)], [0.5, 0.25, 0.0])
        self.df = self.replace_values(self.df, tox21_columns, [(0, 300), (300, 700), (700, 1000)], [0.83, 0.41, 0.0])
        self.df = self.replace_values(self.df, metabolism_columns, [(0, 300), (300, 700), (700, 1000)], [0.71, 0.35, 0.0])
        self.df = self.replace_values(self.df, medicinal_chemistry_columns_float_similar, [(0, 300), (300, 700), (700, 1000)],[0.52, 0.26, 0.0])

        for col in toxicophore_columns:
            self.df[col] = self.df[col].apply(self.substituir_string, args=("['-']", 1.66, 0))

        for col in medicinal_chemistry_columns_str:
            self.df[col] = self.df[col].apply(self.substituir_string, args=("['-']", 0.5, 0))

        for col in absorption_columns_str:
            self.df[col] = self.df[col].apply(self.substituir_string, args=("['-']", 1.2, 0))

        self.df = (
            self.df.assign(
                caco2=pd.to_numeric(self.df['caco2'], errors='coerce').apply(lambda x: 1.1 if x > -5150 else 0),
                PPB=pd.to_numeric(self.df['PPB'], errors='coerce').apply(lambda x: 1.1 if x <= 90 else 0),
                Fu=pd.to_numeric(self.df['Fu'], errors='coerce').apply(lambda x: 1.2 if x >= 5 else 0),
                logVDss=pd.to_numeric(self.df['logVDss'], errors='coerce').apply(lambda x: 1.1 if 40 <= x <= 200 else 0),

                cl_plasma=pd.to_numeric(self.df['cl_plasma'], errors='coerce').apply(lambda x: 5 if 0 <= x <= 5 else (2.5 if 5 < x <= 15 else 0)),
                t_0_5=pd.to_numeric(self.df['t_0_5'], errors='coerce').apply(lambda x: 5 if x > 8 else (2.5 if 1 <= x <= 8 else 0)),

                Lipinski=pd.to_numeric(self.df['Lipinski'], errors='coerce').apply(lambda x: 0.526 if x == 0 else 0),
                Pfizer=pd.to_numeric(self.df['Pfizer'], errors='coerce').apply(lambda x: 0.52 if x == 0 else 0),
                GSK=pd.to_numeric(self.df['GSK'], errors='coerce').apply(lambda x: 0.52 if x == 0 else 0),
                GoldenTriangle=pd.to_numeric(self.df['GoldenTriangle'], errors='coerce').apply(lambda x: 0.5 if x == 0 else 0),
                gasa=pd.to_numeric(self.df['gasa'], errors='coerce').apply(lambda x: 0.52 if x == 1 else 0),

                QED=pd.to_numeric(self.df['QED'], errors='coerce').apply(lambda x: 0.52 if x > 670 else (0.26 if 490 <= x <= 670 else 0)),
                Synth=pd.to_numeric(self.df['Synth'], errors='coerce').apply(lambda x: 0.64 if x <= 6000 else 0),
                Fsp3=pd.to_numeric(self.df['Fsp3'], errors='coerce').apply(lambda x: 0.52 if x >= 420 else 0),
                MCE_18=pd.to_numeric(self.df['MCE_18'], errors='coerce').apply(lambda x: 0.52 if x >= 45000 else 0)
            )
        )

        new_cols = pd.DataFrame({
            'ABSORTION': self.df[absorption_columns + ['caco2']].sum(axis=1, skipna=True),
            'DISTRIBUTION': self.df[['PPB', 'Fu','logVDss'] + distribution_columns].sum(axis=1, skipna=True),
            'TOXICITY': self.df[toxicity_columns].sum(axis=1, skipna=True),
            'TOX21_PATHWAY': self.df[tox21_columns].sum(axis=1, skipna=True),
            'METABOLISM': self.df[metabolism_columns].sum(axis=1, skipna=True),
            'TOXICOPHORE_RULES': self.df[toxicophore_columns].sum(axis=1, skipna=True),
            'EXCRETION': self.df[['cl_plasma', 't_0_5']].sum(axis=1, skipna=True),
            'MEDICINAL_CHEMISTRY': self.df[medicinal_chemistry].sum(axis=1, skipna=True)
        })

        self.df_analysis = pd.concat([self.df, new_cols], axis=1)

        self.df_analysis['SCORE'] = (self.df_analysis['ABSORTION'] * self.weights['ABSORTION'] +
                                     self.df_analysis['DISTRIBUTION'] * self.weights ['DISTRIBUTION'] +
                                     self.df_analysis['TOXICITY'] * self.weights ['TOXICITY'] +
                                     self.df_analysis['TOX21_PATHWAY'] * self.weights ['TOX21_PATHWAY'] +
                                     self.df_analysis['METABOLISM'] * self.weights['METABOLISM'] +
                                     self.df_analysis['TOXICOPHORE_RULES'] * self.weights ['TOXICOPHORE_RULES'] +
                                     self.df_analysis['EXCRETION'] * self.weights['EXCRETION'] +
                                     self.df_analysis['MEDICINAL_CHEMISTRY'] * self.weights['MEDICINAL_CHEMISTRY']) / sum(self.weights.values())
        

        analysis_df = pd.merge(df, self.df_analysis[['smiles'] + self.new_cols_to_move], on='smiles', how='left')
        new_cols = ['ID_Molecula', 'Afinidade'] + self.new_cols_to_move + ['smiles'] + [col for col in analysis_df.columns if col not in self.new_cols_to_move and col not in ['ID_Molecula', 'Afinidade', 'smiles']]

        analysis_df = analysis_df[new_cols]
        analysis_df[self.new_cols_to_move] = analysis_df[self.new_cols_to_move].round(2)

        self.analysis_df = analysis_df

        try:
            self.analysis_df.drop('molstr',axis=1,inplace=True)
        except:
            pass

        self.analysis_df = self.rename(self.analysis_df)      

        for coluna in normalize:
            self.analysis_df[coluna] = self.analysis_df[coluna].apply(self.normalize_values)

        return self.analysis_df

class Extract:

    def __init__(self):
        pass

    RDLogger.DisableLog('rdApp.*')

    def extract_ids_affinities_from_sdf(self, sdf_file):
        ids_affinity = []
        with Chem.SDMolSupplier(sdf_file) as suppl:
            for mol in suppl:
                if mol is not None:
                    mol_id = mol.GetProp('_Name')
                    affinity = mol.GetDoubleProp('minimizedAffinity')
                    smiles = Chem.MolToSmiles(mol)
                    ids_affinity.append((mol_id, affinity, smiles))
        df = pd.DataFrame(ids_affinity, columns=['ID_Molecula', 'Afinidade', 'smiles'])
        return df

    def extract (self,csv_file, sdf_file ):

        try:
            df_final = self.extract_ids_affinities_from_sdf(sdf_file)
        except:
            print('\nSDF NOT FOUND\n')
            sys.exit()

        try:
            df_csv = pd.read_csv(csv_file)

        except:
            print('\nCSV NOT FOUND\n')
            sys.exit()
    
        df_merged = pd.merge(df_final, df_csv, on='smiles', how='left')

        df_merged.drop_duplicates(subset=['smiles'], inplace=True)
        
        return df_merged

class Output:

    def __init__(self):
        pass


    def conditional_formatting(self,df,excel_path):

        writer = pd.ExcelWriter(excel_path, engine="xlsxwriter")

        df.to_excel(writer, sheet_name="Sheet1", index=False)

        workbook = writer.book
        worksheet = writer.sheets["Sheet1"]

        (max_row, max_col) = df.shape

        green_format = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})
        yellow_format = workbook.add_format({'bg_color': '#FFEB9C', 'font_color': '#9C5700'})
        red_format = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
        gray_format = workbook.add_format({'bg_color': '#D3D3D3'})

        columns = [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 125, 126, 127, 128, 129, 131]

        string_columns = [32, 33, 34, 35, 117, 118, 119, 120, 121, 122, 123, 124]

        gray_columns = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 31, 40, 41, 42, 43, 44, 45, 46, 48, 81, 82, 83, 84, 130]


        special_conditions = {
            38: [(0, 0, green_format), (1, float('inf'), red_format)],
            39: [(0, 0, green_format), (1, float('inf'), red_format)],
            26: [(1, 1, green_format), (0, 0, red_format)],
            28: [(float('-inf'), 6000, green_format), (6000.01, float('inf'), red_format)],
            36: [(float('-inf'), 0, green_format), (1, float('inf'), red_format)],
            37: [(float('-inf'), 0, green_format), (1, float('inf'), red_format)],
            47: [(-5150, float('inf'), green_format), (float('-inf'), -5150.01, red_format)],
            27: [(670, float('inf'), green_format), (490, 669.99, yellow_format), (float('-inf'), 489.99, red_format)],
            80: [(8, float('inf'), green_format), (1, 7.9, yellow_format), (float('-inf'), 0, red_format)],
            62: [(float('-inf'), 90, green_format), (90.01, float('inf'), red_format)],
            29: [(420, float('inf'), green_format), (float('-inf'), 419, red_format)],
            30: [(45000, float('inf'), green_format), (float('-inf'), 44999.99, red_format)],
            64: [(5, float('inf'), green_format), (float('-inf'), 4.99, red_format)],
            79: [(0, 5, green_format), (5.01, 15, yellow_format), (15.01, float('inf'), red_format)],
            63: [(40, 200, green_format), (float('-inf'), 39.99, red_format), (200.01, float('inf'), red_format)]
        }

        def get_column_letter(col_idx):
            letter = ''
            while col_idx > 0:
                col_idx, remainder = divmod(col_idx - 1, 26)
                letter = chr(65 + remainder) + letter
            return letter

        for col in columns:
            col_letter = get_column_letter(col + 1)
            cell_range = f'{col_letter}2:{col_letter}{max_row + 1}'
            
            worksheet.conditional_format(cell_range, {'type': 'cell', 'criteria': 'between', 'minimum': 0, 'maximum': 300, 'format': green_format})
            worksheet.conditional_format(cell_range, {'type': 'cell', 'criteria': 'between', 'minimum': 300.01, 'maximum': 700, 'format': yellow_format})
            worksheet.conditional_format(cell_range, {'type': 'cell', 'criteria': 'between', 'minimum': 700.01, 'maximum': 1000, 'format': red_format})

        for col in string_columns:
            col_letter = get_column_letter(col + 1)
            cell_range = f'{col_letter}2:{col_letter}{max_row + 1}'

            worksheet.conditional_format(cell_range, {'type': 'text', 'criteria': 'containing', 'value': "['-']", 'format': green_format})
            worksheet.conditional_format(cell_range, {'type': 'text', 'criteria': 'not containing', 'value': "['-']", 'format': red_format})

        for col, conditions in special_conditions.items():
            col_letter = get_column_letter(col + 1)  # Adicionar 1 porque as colunas são 1-indexadas no Excel
            cell_range = f'{col_letter}2:{col_letter}{max_row + 1}'

            for min_val, max_val, fmt in conditions:
                criteria = 'between'
                if min_val == float('-inf'):
                    criteria = 'less than or equal to'
                    min_val = max_val
                elif max_val == float('inf'):
                    criteria = 'greater than or equal to'
                    max_val = min_val

                worksheet.conditional_format(cell_range, {'type': 'cell', 'criteria': criteria, 'minimum': min_val, 'maximum': max_val, 'format': fmt})
    
        for col in gray_columns:
            col_letter = get_column_letter(col + 1)  # Adicionar 1 porque as colunas são 1-indexadas no Excel
            cell_range = f'{col_letter}2:{col_letter}{max_row + 1}'

            worksheet.conditional_format(cell_range, {'type': 'no_blanks', 'format': gray_format})

        writer.close()

    def output(self, df):

        if ((df['SCORE'] == 0).any() or (df['ABSORTION'] == 0).any() or (df['DISTRIBUTION'] == 0).any()):
            print('\nInput files are not correlated\n')
            return None
        
        print('\nAnalysis completed')

        if not os.path.exists('score'):
            os.makedirs('score')

        excel_path = os.path.join('score', 'scoreadmet.xlsx')

        if os.path.exists(excel_path):
            existing_df = pd.read_excel(excel_path, sheet_name='Sheet1')
            initial_count = len(existing_df)
            updated_df = pd.concat([existing_df, df], ignore_index=True)
            updated_df = updated_df.sort_values(by='SCORE', ascending=False)
            updated_df.drop_duplicates(subset='smiles', keep="first", inplace=True)
            final_count = len(updated_df)
            new_entries = final_count - initial_count
            print(f'{new_entries} new molecules were added.\n')
        else:
            updated_df = df
            updated_df = updated_df.sort_values(by='SCORE', ascending=False)
            updated_df.drop_duplicates(subset='smiles', keep='first', inplace=True)
            final_count = len(updated_df)
            print(f'The spreadsheet was created with {final_count} molecules.\n')

        self.conditional_formatting(updated_df,excel_path)

        return updated_df




