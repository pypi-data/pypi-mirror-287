#   A program for converting PubMed output to a flat text file or data frame
#   Copyright (C) 2019, 2024 Ray Griner (rgriner_fwd@outlook.com)
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#------------------------------------------------------------------------------

"""Convert PubMed output to a flat text file or data frame

SUMMARY
-------
A simple package for converting PubMed output with all PubMed fields into a
flat file or pandas.DataFrame. Simple functions are provided to merge the
results of separate searches and automatically create tags (variables that
are 'Y' or '') to indicate which search(es) a reference is found in.

Users can then add notes on the references by importing the flat file into
a spreadsheet program and adding their notes in new columns. A user can then
export this spreadsheet back to a flat file, convert it to a data frame,
merge it with the results of additional searches, and convert this merged
data frame back to a text file for further user notes, etc...

Obviously this is not a particularly robust 'database system' to use, and in
particular users should take care that when updating flat files they do not
omit any columns they manually created in the previous flat file.

TRADEMARK NOTICE
----------------
The PubMed wordmark is a registered trademark of the U.S. Department of
Health and Human Services. This software is not endorsed by or affiliated
with the trademark holders.

EXAMPLE
-------
import flatmed as fm

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
master_df = master_df[~( (master_df.lta_MSM_excl == 'Y'))]

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

"""

#------------------------------------------------------------------------------
# File:    __init__.py
# Date:    2024-07-29
# Author:  Ray Griner
# Changes:
#------------------------------------------------------------------------------
__author__ = 'Ray Griner'
__version__ = '0.0.1'
#__all__ = ['']

from .flatmed import pubmed_to_df, merge_to_df, txt_to_df, df_to_txt
