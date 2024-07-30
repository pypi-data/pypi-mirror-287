# Summary
A simple package for converting PubMed output with all PubMed fields into a
flat file or `pandas.DataFrame` object. Simple functions are provided to
merge the results of separate searches and automatically create tags
(variables that are 'Y' or '') to indicate which search(es) a reference is
found in.

Users can then add notes on the references by importing the flat file into
a spreadsheet program and adding their notes in new columns. A user can then
export this spreadsheet back to a flat file, convert it to a data frame,
merge it with the results of additional searches, and convert this merged
data frame back to a text file for further user notes, etc...

Obviously this is not a particularly robust 'database system' to use, and in
particular users should take care that when updating flat files they do not
omit any columns they manually created in the previous flat file.

# Trademark Notice
The PubMed wordmark is a registered trademark of the U.S. Department of
Health and Human Services. This software is not endorsed by or affiliated
with the trademark holders.

# Example
```
import flatmed as fm

# When rerunning, uncomment the `txt_to_df` call and change the next lines
# to a `merge_to_df()` call.
#master_df = fm.txt_to_df('ex_refs_mynotes.txt')
inpdir = 'downloaded/'

# Start with a single set of results and convert to a data frame
master_df = fm.pubmed_to_df(inpdir + 'TMLE.txt')
master_df['lta_TMLE'] = 'Y'

# Merge to this data frame four other searches using the default merge 
#   method (outer join) and create four more indicator variables.
master_df = fm.merge_to_df(master_df, inpdir + 'MSM.txt', 'lta_MSM')
master_df = fm.merge_to_df(master_df, inpdir + 'TVCONF.txt', 'lta_TVCONF')
master_df = fm.merge_to_df(master_df, inpdir + 'AIPW.txt', 'lta_AIPW')
master_df = fm.merge_to_df(master_df, inpdir + 'MSM_excl.txt',
                           'lta_MSM_excl')

# The `lta_MSM_excl` are a subset of the MSM results that we have already
#  determined can be excluded.
master_df = master_df[~((master_df.lta_MSM_excl == 'Y'))]

# After the above filter, the variable is always empty, so can be dropped.
master_df = master_df.drop(columns = ['lta_MSM_excl'])

# publication year
master_df['l_pubyear'] = master_df.DP.str.slice(start=0, stop=4)

# keep only a subset of the PubMed fields. Can add more if desired.
# We use the convention that any variables automatically created as a tag
# starts with 'lta_' and other variables we create (either externally or in
# this file) start with 'l_'.
my_cols = [ x for x in master_df.columns if x.startswith('lta_')
                                            or x.startswith('l_') ]
fm.df_to_txt(master_df, 'ex_refs.txt',
             ['PMID', 'TI', 'AU', 'SO', 'l_pubyear'] + my_cols + ['AB'])
```

# Release Notes
## Version 0.0.1
- Initial release
