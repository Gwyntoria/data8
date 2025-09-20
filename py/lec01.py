"""
## Get data from web
The following is a tiny program to download text from the web.
"""

import os
import re
from urllib.request import urlopen

import numpy as np
import matplotlib.pyplot as plt
from datascience import Table


# A tiny program to download text from the web.
def read_url(url):
    return re.sub("\\s+", " ", urlopen(url).read().decode())


# Function to calculate cumulative sum
def cumulative_sum(table: Table) -> Table:
    """
    Returns a new Table with each column replaced by its cumulative sum.
    """
    labels = table.labels
    columns = [np.cumsum(np.array(col)) for col in table.columns]
    return Table().with_columns(list(sum(zip(labels, columns), ())))


# If running this script directly, you might want to add functionality to display the plots
if __name__ == "__main__":
    """
    ## 1. Get data from web
    """
    # Download Huckleberry Finn text
    huck_finn_url = "https://www.inferentialthinking.com/data/huck_finn.txt"
    huck_finn_text = read_url(huck_finn_url)
    huck_finn_chapters_list = huck_finn_text.split("CHAPTER ")[44:]
    huck_finn_chapters_num = len(huck_finn_chapters_list)

    # Download Little Women text
    little_women_url = "https://www.inferentialthinking.com/data/little_women.txt"
    little_women_text = read_url(little_women_url)
    little_women_chapters_list = little_women_text.split("CHAPTER ")[1:]
    little_women_chapters_num = len(little_women_chapters_list)

    print(f"Number of Huckleberry Finn chapters: {huck_finn_chapters_num}")
    print(f"Number of Little Women chapters: {little_women_chapters_num}")

    """
    ## 2. Working with Tables
    A lot of data science is about transforming data often to produce tables that we can more easily analyze.
    In this class you will use the Berkeley datascience library to manipulate and data.
    """

    # Create a table with Huckleberry Finn chapters
    huck_finn_table = Table().with_column("Chapters", huck_finn_chapters_list)

    # Count character mentions in Huckleberry Finn
    tom_counts = np.char.count(huck_finn_chapters_list, "Tom")
    jim_counts = np.char.count(huck_finn_chapters_list, "Jim")
    huck_counts = np.char.count(huck_finn_chapters_list, "Huck")

    print(f"tom_counts(in first 5 chapters):    {tom_counts[:5]}")
    print(f"jim_counts(in first 5 chapters):    {jim_counts[:5]}")
    print(f"huck_counts(in first 5 chapters):   {huck_counts[:5]}")

    character_counts_table = Table().with_columns(
        [
            "Tom",
            tom_counts,
            "Jim",
            jim_counts,
            "Huck",
            huck_counts,
        ]
    )

    """
    ## 3. We will Learn to Visualize Data
    Plot the cumulative counts: How many times in Chapter 1, how many times in Chapters 1 and 2, and so on.
    """

    # Create plots directory if it doesn't exist
    plots_dir = "plots"
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
        print(f"Created directory '{plots_dir}' for saving plots")

    # Set plotting style
    plt.style.use("fivethirtyeight")
    cum_character_counts_table = cumulative_sum(character_counts_table).with_column(
        "Chapter",
        np.arange(1, huck_finn_chapters_num + 1, 1),
    )
    cum_character_counts_table.plot(column_for_xticks="Chapter", width=10, height=10)
    plt.title("Cumulative Number of Times Name Appears")
    plt.savefig(os.path.join(plots_dir, "1_huck_finn_character_mentions.png"))
    plt.close()

    # The chapters of Little Women
    little_women_table = Table().with_column("Chapters", little_women_chapters_list)

    # Counts of names in the chapters of Little Women
    names = ["Amy", "Beth", "Jo", "Laurie", "Meg"]
    mentions = {name: np.char.count(little_women_chapters_list, name) for name in names}
    counts_lw = Table().with_columns(
        [
            "Amy",
            mentions["Amy"],
            "Beth",
            mentions["Beth"],
            "Jo",
            mentions["Jo"],
            "Laurie",
            mentions["Laurie"],
            "Meg",
            mentions["Meg"],
        ]
    )

    # Plot the cumulative counts
    Table.static_plots()
    character_cum_counts_lw = cumulative_sum(counts_lw).with_column(
        "Chapter", np.arange(1, little_women_chapters_num + 1, 1)
    )
    character_cum_counts_lw.plot(column_for_xticks="Chapter", width=10, height=10)
    plt.title("Cumulative Number of Times Name Appears")
    plt.savefig(os.path.join(plots_dir, "2_little_women_character_mentions.png"))
    plt.close()

    """
    ## 4. Examining Length
    How long are the books? How long are sentences?
    """

    # In each chapter, count the number of all characters;
    # call this the "length" of the chapter.
    # Also count the number of periods.

    huck_finn_length = len(huck_finn_text)
    hf_period_counts_list = np.char.count(huck_finn_chapters_list, ".")
    hf_chapter_length_list = [len(chapter) for chapter in huck_finn_chapters_list]
    hf_period_counts_sum = sum(hf_period_counts_list)

    print(f"Total length of Huckleberry Finn: {huck_finn_length} characters")
    print(f"Total number of periods in Huckleberry Finn: {hf_period_counts_sum}")

    # Calculate chapter lengths and period counts
    hf_length_period_table = Table().with_columns(
        [
            "Periods",
            hf_period_counts_list,
            "Length",
            hf_chapter_length_list,
        ]
    )

    little_women_length = len(little_women_text)
    lw_period_counts_list = np.char.count(little_women_chapters_list, ".")
    lw_chapter_length_list = [len(chapter) for chapter in little_women_chapters_list]
    lw_period_counts_sum = sum(lw_period_counts_list)

    print(f"Total length of Little Women: {little_women_length} characters")
    print(f"Total number of periods in Little Women: {lw_period_counts_sum}")

    lw_length_period_table = Table().with_columns(
        [
            "Periods",
            lw_period_counts_list,
            "Length",
            lw_chapter_length_list,
        ]
    )

    print(
        f"Average number of characters per period: {(huck_finn_length + little_women_length) / (hf_period_counts_sum + lw_period_counts_sum):.1f}"
    )

    Table.static_plots()
    plt.figure(figsize=(14, 14))
    plt.xlabel("Number of periods in chapter")
    plt.ylabel("Number of characters in chapter")
    plt.scatter(x=hf_length_period_table[0], y=hf_length_period_table[1], color="r")
    plt.scatter(x=lw_length_period_table[0], y=lw_length_period_table[1], color="b")

    # Combine period counts from both books
    combined_period_counts = (
        hf_period_counts_list.tolist() + lw_period_counts_list.tolist()
    )

    # Combine chapter lengths from both books
    combined_chapter_lengths = hf_chapter_length_list + lw_chapter_length_list

    # Add linear fit
    fit = np.polyfit(combined_period_counts, combined_chapter_lengths, 1)
    fit_func = np.poly1d(fit)
    plt.plot(
        hf_length_period_table[0],
        fit_func(hf_length_period_table[0]),
        color="g",
        label="Fit",
    )

    plt.legend()
    plt.savefig(os.path.join(plots_dir, "3_chapter_length_comparison.png"))
    plt.close()

    """
    ## 5. Examining distributions
    """

    Table.static_plots()
    hf_length_period_table.with_column(
        "Sentence Length",
        hf_length_period_table["Length"] / hf_length_period_table["Periods"],
    ).hist("Sentence Length", width=10, height=10)
    plt.title("Huckleberry Finn Sentence Lengths")
    plt.savefig(os.path.join(plots_dir, "4_huck_finn_sentence_lengths.png"))
    plt.close()

    Table.static_plots()
    lw_length_period_table.with_column(
        "Sentence Length",
        lw_length_period_table["Length"] / lw_length_period_table["Periods"],
    ).hist("Sentence Length", width=10, height=10)
    plt.title("Little Women Sentence Lengths")
    plt.savefig(os.path.join(plots_dir, "5_little_women_sentence_lengths.png"))
    plt.close()
