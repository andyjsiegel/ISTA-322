import pandas as pd
import re
import os
print(os.getcwd())

def parse_overwatch_stats(file_path):
    hero_stats = []

    with open(file_path, 'r') as f:
        content = f.read()

    # The data starts after the line containing 'Region' and before 'FREQUENTLY ASKED QUESTIONS'
    start_marker = 'Region\nAmericasAsiaEurope\n\nHeroPick RateWin Rate\n'
    end_marker = '\nFREQUENTLY ASKED QUESTIONS'

    start_index = content.find(start_marker)
    end_index = content.find(end_marker)

    if start_index != -1 and end_index != -1:
        # Adjust start_index to get right after the header line
        data_string = content[start_index + len(start_marker):end_index].strip()
        
        # Split the data string by lines
        lines = data_string.split('\n')
        
        # Process lines in chunks of 3: HeroName, Pick Rate, Win Rate
        for i in range(0, len(lines), 3):
            if i + 2 < len(lines):
                hero_name = lines[i].strip()
                pick_rate_str = lines[i+1].strip()
                win_rate_str = lines[i+2].strip()
                
                # Clean and convert to float
                pick_rate = float(pick_rate_str.replace('%', ''))
                win_rate = float(win_rate_str.replace('%', ''))
                
                hero_stats.append({
                    'Hero': hero_name,
                    'Pick Rate (%)': pick_rate,
                    'Win Rate (%)': win_rate
                })

    ow_ranked_df = pd.DataFrame(hero_stats)
    return ow_ranked_df

if __name__ == "__main__":
    snapshot_file_path = '/Users/andysiegel/Library/CloudStorage/GoogleDrive-andyjsiegel1@gmail.com/My Drive/University/Semester 5/ISTA 322/Final Project/overwatch_hero_stats_snapshot.html'
    ow_ranked_df = parse_overwatch_stats(snapshot_file_path)

    print('First 5 rows of the Overwatch Ranked Stats dataset:')
    print(ow_ranked_df.head())

    print('\nOverwatch Ranked Stats DataFrame Info:')
    ow_ranked_df.info()
