import pandas as pd

excel_file = "D:\\Python\\Pandas ex\\Names.xlsx"

folder_a_df = pd.read_excel(excel_file, sheet_name="Folder A")
folder_b_df = pd.read_excel(excel_file, sheet_name="Folder B")

folder_a = set(folder_a_df.iloc[:, 1].dropna())
folder_b = set(folder_b_df.iloc[:, 1].dropna())

common_images = folder_a.intersection(folder_b)
unique_to_folder_a = folder_a.difference(folder_b)

data = {
    "Common Images": list(common_images),
    "Unique to Folder A": list(unique_to_folder_a)
}

df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))

output_path = "D:\\Python\\Pandas ex\\image_comparison_results.xlsx"
df.to_excel(output_path, index=False)

print(f"Comparison results have been exported to '{output_path}'")