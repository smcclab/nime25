#!/usr/bin/env python
import requests
import pandas as pd
import tomllib
pd.options.mode.copy_on_write = True

with open("secrets.toml", "rb") as f:
    secrets = tomllib.load(f)

# This is the ID of the google sheet we are downloading.
google_sheet_id = secrets["gs_sheet_id"]  # Extract this from the URL of your Google Sheet
# The gid values are ID for each tab in the spreadsheet
# To find the gid values, open your Google Sheet and look at the URL when you click on each tab
papers_gid = secrets["papers_gid"]  # Replace with actual gid for the "papers" sheet
music_gid = secrets["music_gid"]  # Replace with actual gid for the "music" sheet
workshops_gid = secrets["workshops_gid"]  # Replace with actual gid for the "workshops" sheet

print("Going to download the NIME2025 proceedings spreadsheets...")

def download_specific_google_sheet_as_csv(sheet_id, gid, output_file="data.csv"):
    """
    Downloads a specific sheet from a Google Sheets document as CSV
    
    Parameters:
    sheet_id (str): The ID of the Google Sheet (from the URL)
    gid (str): The GID of the specific sheet to download
    output_file (str): The name of the output CSV file
    
    Returns:
    bool: True if successful, False otherwise
    """
    # Construct the export URL with the gid parameter
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
    
    try:
        # Get the content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Write the content to a file
        with open(output_file, 'wb') as f:
            f.write(response.content)
        
        print(f"Successfully downloaded sheet with gid {gid} to {output_file}")
        return True
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading sheet: {e}")
        return False


# Download each sheet
download_specific_google_sheet_as_csv(google_sheet_id, papers_gid, "gs_papers.csv")
download_specific_google_sheet_as_csv(google_sheet_id, music_gid, "gs_music.csv")
download_specific_google_sheet_as_csv(google_sheet_id, workshops_gid, "gs_workshops.csv")
papers_df = pd.read_csv("gs_papers.csv")
music_df = pd.read_csv("gs_music.csv")
workshops_df = pd.read_csv("gs_workshops.csv")

print("Now going to combine them all together to make one proceedings csv to rule them all.")

proc_cols = ["id","track","format","type","session_code","session_name","session_position","duration","presence","speaker","title","authors","abstract","paper_url","video_url","slides_url","image_url"]

# Function to filter dataframes to only include needed columns
def filter_columns(df, needed_cols):
    # Find columns that exist in both the dataframe and the needed columns list
    available_cols = [col for col in needed_cols if col in df.columns]
    # Return dataframe with only those columns
    return df[available_cols]

# Filter each dataframe to only include the columns in proc_cols
papers_filtered = filter_columns(papers_df, proc_cols)
papers_filtered['id'] = papers_filtered['id'].astype(int)

music_filtered = filter_columns(music_df, proc_cols)
music_filtered['id'] = music_filtered['id'].astype(int)

workshops_filtered = filter_columns(workshops_df, proc_cols)
workshops_filtered['id'] = workshops_filtered['id'].astype(int)

# Concatenate the filtered dataframes
proceedings_df = pd.concat([papers_filtered, music_filtered, workshops_filtered], ignore_index=True)

proceedings_df['id'] = proceedings_df['id'].astype(int)
proceedings_df['image_url'] = proceedings_df['id'].apply(lambda x: f"{x}.jpg")
proceedings_df['paper_url'] = proceedings_df['id'].apply(lambda x: f"nime2025_{x}.pdf")

# Output to CSV
proceedings_df.to_csv('../_data/proceedings.csv', index=False)
print("all done!")
