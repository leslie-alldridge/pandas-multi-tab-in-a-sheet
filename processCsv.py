import pandas as pd

xls = pd.ExcelFile('Xero4.xls')

# Now you can list all sheets in the file
print(xls.sheet_names)

# to read all sheets to a map
sheet_to_df_map = {}
for sheet_name in xls.sheet_names:
    try:
        sheet_to_df_map[sheet_name] = xls.parse(sheet_name)

        is_vote = sheet_to_df_map[sheet_name]['Status']=='Vote'
        sum_active_votes = sheet_to_df_map[sheet_name][is_vote]["Votes"].astype(int).sum()

        sum_votes = sheet_to_df_map[sheet_name]['Votes'].astype(int).sum()
        print(f'{sum_active_votes}')
        # you can also use sheet_index [0,1,2..] instead of sheet name.
    except:
        continue    
    