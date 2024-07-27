from .models import *  # COLOCAR O PONTO
import json
import argparse
from argparse import RawTextHelpFormatter
import pandas as pd

header = """LAMBDA - Laboratório Multiusuário e Analise de Dados

    Júlio César Albuquerque Xavier
    Edson Luiz Folador"""

def main():

    parser = argparse.ArgumentParser(description=header,formatter_class=RawTextHelpFormatter)

    subparsers = parser.add_subparsers(dest='tool', required=True, help="""The ADMETSCORE is a software that aims to facilitate the ADMET analysis of molecules resulting from pharmacophore research. The tool is divided into two main parts:
                                       """)

    parser_sdf = subparsers.add_parser('sdf',description=header + '\n''\nThis module partitions the Pharmit docking file. This is necessary to submit each partitioned file to the ADMETlab 3.0 screening, allowing for ADMET analysis of these molecules. Each part will need to be screened individually.',formatter_class=RawTextHelpFormatter, help="""This component allows the splitting of an SDF file resulting from Pharmit Search docking (https://pharmit.csb.pitt.edu/search.html) into multiple smaller files. Each SDF file contains 299 molecules by default, though this number can be adjusted via a parameter. This splitting is necessary for screening in ADMETLab 3.0 (https://admetlab3.scbdd.com/). Users can then upload each file to the ADMETLab site and download the results, proceeding to the second component of the tool, SCORE.
  ↳  More information about the parameters: admetscore sdf -h
                                       """)

    parser_sdf.add_argument('-i', '--input_file', type=str, required=True, help='(required): The Pharmit docking file (SDF) that will be partitioned.\n''\n')
    parser_sdf.add_argument('-db', '--database', type=str, required=True, help='(required): The database used for docking in Pharmit. Enter the name exactly as it appears on the website. Each partition will be named with the database name and a numerical identifier\n''\n')
    parser_sdf.add_argument('-n', '--batch', type=int, default=299, help='(optional): Use this parameter if you want to change the number of molecules in each part. This is useful if the ADMETlab 3.0 website accepts more or fewer molecules per screening. The default is set to 300\n''\n')
    parser_sdf.add_argument('-sd', '--pharmit_score_docking', type=float, help=' (optional): Use this parameter to work with a specific docking score from Pharmit. This will reduce the number of partitions created from the SDF, as by default the entire SDF file is partitioned.\n''\n')

    parser_score = subparsers.add_parser('score',description=header+ '\n''\n''After using the SDF module and screening each partition with ADMETlab 3.0, you can then provide this module with one partition of the SDF along with the CSV result file for that partition from ADMETlab 3.0. This will create a folder named score, which will contain a spreadsheet with the ADMET analysis for each molecule in the partition. This spreadsheet assigns a score from 0 to 10 to each molecule, where a higher score indicates better performance in the ADMET analysis. The spreadsheet is cumulative and will accumulate results from each partition you process.',formatter_class=RawTextHelpFormatter, help="""This component uses the results from ADMETLab 3.0 to create an analysis spreadsheet. It assigns scores to each ADMET analysis group, weights these groups, and ranks the best molecules. Additionally, it integrates information from the SDF file downloaded from Pharmit into the spreadsheet, generating a file with details. There is also a parameter to generate a new file with only the top-performing molecules, and another parameter to adjust the weights of each group.
  ↳  More information about the parameters: admetscore score -h""")

    parser_score.add_argument('-i', '--input_file', type=str, required=True, help='(required): The CSV file resulting from the ADMETlab 3.0 analysis of the partition to be analyzed.\n''\n')
    parser_score.add_argument('-s', '--sdf', type=str, required=True, help='(required): The SDF partition that was analyzed by ADMETlab 3.0. The module will not accept any other partition if the CSV file does not match the corresponding ADMETlab 3.0 analysis for that partition.\n''\n')
    parser_score.add_argument('-t', '--best_hits', type=int, default=None, help='(optional): Specify the number of top-scoring molecules you want to view. The spreadsheet will be non-cumulative and a separate file will be created in the score folder.\n''\n')
    parser_score.add_argument('-w', '--weights',
                    type=str,
                    help="""(optional): If you want to adjust the parameters for the ADMETlab 3.0 analysis, the default weights are as follows. To change the weights, create a .json file with a dictionary that uses the exact names of the ADMET analysis categories, modifying only their weight values.
{
"ABSORPTION": 2,
"DISTRIBUTION": 1,
"TOXICITY": 8,
"TOX21_PATHWAY": 3,
"METABOLISM": 2,
"TOXICOPHORE_RULES": 3,
"EXCRETION": 1,
"MEDICINAL_CHEMISTRY": 5
}
""")

    args = parser.parse_args()

    if args.tool == 'sdf':
        process_sdf(args.input_file, args.database, args.batch, args.pharmit_score_docking)

    elif args.tool == 'score':
        process_score(args.input_file, args.sdf, args.best_hits, args.weights)

def process_sdf(input_file, database, batch, pharmit_score):

    sdf_instance = Sdf()

    sdf_instance.process_sdf(input_file, database, batch, pharmit_score)

def process_score(input_file, sdf, best_hits, weights):

    if weights is not None:
        with open(weights, "r", encoding="utf-8") as f:
            weights = json.loads(f.read())
    
    extract_instance = Extract()
    analysis_instance = AdmetSpreadsheet()
    output_instance = Output()

    df = extract_instance.extract(input_file, sdf)
    df = analysis_instance.process_data(df, weights)

    df = output_instance.output(df)

    if best_hits is not None:
        excel_top_path = os.path.join('score', f'scoreadmet_{best_hits}_tops.xlsx')
        top_df = df.head(best_hits)
        output_instance.conditional_formatting(top_df,excel_top_path)
        print(f'↳ File with the {best_hits} best molecules was created\n')

if __name__ == '__main__':
    main()
