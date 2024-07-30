#------------------------------------------------------------------------------
#   A program for converting PubMed output to a flat text file or data frame
#   Copyright (C) 2024 Ray Griner (rgriner_fwd@outlook.com)
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

#------------------------------------------------------------------------------
# File: flatmed.py
# Date: 2024-07-27
# Author: Ray Griner
# Purpose: Support for converting PubMed-style output from PubMed to a
#   file that is one record per PubMed entry with all fields included. An
#   update file can be merged with a master file or data frame that is already
#   one record per PubMed entry.
#------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import copy
from dataclasses import dataclass
from typing import Optional

@dataclass(slots=True)
class SingleRec:
    '''Dataclass representing a single entry in the PubMed database.

    Attributes of this class are PubMed fields. If a field appears more than
    once for a given PubMed entry (e.g., the 'AU' field stores information
    about a single author and usually appears more than once), then all values
    for the PubMed field are concatenated in the order they appeared in the
    input using '; ' as delimiter.

    Attributes
    ----------
    All attributes are type `str`. and were taken from the union of lists
      at:
      (1) https://www.nlm.nih.gov/bsd/mms/medlineelements.html, and
      (2) https://pubmed.ncbi.nlm.nih.gov/help/.

    Attributes from (1) are: AB, AD, AID, AU, AUID, BTI, CI, CIN, CN, COIS,
      CON, CRDT, CRF, CRI, CTI, DA, DCOM, DDIN, DEP, DP, DRIN, ECF, ECI,
      ED, EDAT, EFR, EIN, EN, FAU, FED, FIR, FPS, GN, GR, GS, IP, IR, IRAD,
      IS, ISBN, JID, JT, LA, LID, LR, MH, MHDA, MID, NM, OAB, OCI, OID,
      ORI, OT, OTO, OWN, PG, PHST, PL, PMC, PMCR, PMID, PS, PST, PT, PUBM,
      RF, RIN, RN, ROF, RPF, RPI, SB, SFM, SI, SO, SPIN, STAT, TA, TI, TT,
      UIN, UOF, VI, VTI.

    Attributes from (2) and not (1) are: COI, CP, CTDT, DRDT, OABL, PB,
      RRI, RRF.

    Refer to the listed websites for the meanings of each attribute.

    Trademark Notice
    ----------------
    The PubMed wordmark is a registered trademark of the U.S. Department of
    Health and Human Services. This software is not endorsed by or affiliated
    with the trademark holders.
    '''
    # https://www.nlm.nih.gov/bsd/mms/medlineelements.html
    AB  : str; AD  : str; AID : str; AU  : str
    AUID: str; BTI : str; CI  : str; CIN : str
    CN  : str; COIS: str; CON : str; CRDT: str
    CRF : str; CRI : str; CTI : str; DA  : str
    DCOM: str; DDIN: str; DEP : str; DP  : str
    DRIN: str; ECF : str; ECI : str; ED  : str
    EDAT: str; EFR : str; EIN : str; EN  : str
    FAU : str; FED : str; FIR : str; FPS : str
    GN  : str; GR  : str; GS  : str; IP  : str
    IR  : str; IRAD: str; IS  : str; ISBN: str
    JID : str; JT  : str; LA  : str; LID : str
    LR  : str; MH  : str; MHDA: str; MID : str
    NM  : str; OAB : str; OCI : str; OID : str
    ORI : str; OT  : str; OTO : str; OWN : str
    PG  : str; PHST: str; PL  : str; PMC : str
    PMCR: str; PMID: str; PS  : str; PST : str
    PT  : str; PUBM: str; RF  : str; RIN : str
    RN  : str; ROF : str; RPF : str; RPI : str
    SB  : str; SFM : str; SI  : str; SO  : str
    SPIN: str; STAT: str; TA  : str; TI  : str
    TT  : str; UIN : str; UOF : str; VI  : str
    VTI : str

    # https://pubmed.ncbi.nlm.nih.gov/help/, not in the above
    COI : str; CP  : str; CTDT: str; DRDT: str
    OABL: str; PB  : str; RRI : str; RRF : str

    def __init__(self):
        '''The constructor takes no parameters. All attributes are set to
        the empty string initially.
        '''

    def reset(self):
        '''Reset all attributes to the empty string.
        '''
        self.AB   = ''; self.AD   = ''; self.AID  = ''; self.AU   = ''
        self.AUID = ''; self.BTI  = ''; self.CI   = ''; self.CIN  = ''
        self.CN   = ''; self.COIS = ''; self.CON  = ''; self.CRDT = ''
        self.CRF  = ''; self.CRI  = ''; self.CTI  = ''; self.DA   = ''
        self.DCOM = ''; self.DDIN = ''; self.DEP  = ''; self.DP   = ''
        self.DRIN = ''; self.ECF  = ''; self.ECI  = ''; self.ED   = ''
        self.EDAT = ''; self.EFR  = ''; self.EIN  = ''; self.EN   = ''
        self.FAU  = ''; self.FED  = ''; self.FIR  = ''; self.FPS  = ''
        self.GN   = ''; self.GR   = ''; self.GS   = ''; self.IP   = ''
        self.IR   = ''; self.IRAD = ''; self.IS   = ''; self.ISBN = ''
        self.JID  = ''; self.JT   = ''; self.LA   = ''; self.LID  = ''
        self.LR   = ''; self.MH   = ''; self.MHDA = ''; self.MID  = ''
        self.NM   = ''; self.OAB  = ''; self.OCI  = ''; self.OID  = ''
        self.ORI  = ''; self.OT   = ''; self.OTO  = ''; self.OWN  = ''
        self.PG   = ''; self.PHST = ''; self.PL   = ''; self.PMC  = ''
        self.PMCR = ''; self.PMID = ''; self.PS   = ''; self.PST  = ''
        self.PT   = ''; self.PUBM = ''; self.RF   = ''; self.RIN  = ''
        self.RN   = ''; self.ROF  = ''; self.RPF  = ''; self.RPI  = ''
        self.SB   = ''; self.SFM  = ''; self.SI   = ''; self.SO   = ''
        self.SPIN = ''; self.STAT = ''; self.TA   = ''; self.TI   = ''
        self.TT   = ''; self.UIN  = ''; self.UOF  = ''; self.VI   = ''
        self.VTI  = ''

        self.COI  = ''; self.CP   = ''; self.CTDT = ''; self.DRDT = ''
        self.OABL = ''; self.PB   = ''; self.RRI  = ''; self.RRF  = ''

def pubmed_to_df(filename, unexpected_attr = 'print') -> pd.DataFrame:
    '''Parse PubMed-style output from file and convert to a data frame.

    The data frame will have one column with type='str' per PubMed field.
    If a PubMed entry has multiple values for a given field (e.g., for the
    `AU` field that represents a single author), the values are
    concatenated with '; ' as delimiter in the order they appear in the
    input file.

    Only PubMed fields that are attributes of `SingleRec` are supported.
    This is meant to inclue all PubMed fields, but if a PubMed field
    is encountered that is not an attribute of this class, the field is not
    included in the output, and a message is optionally generated
    according to the `unexpected_attr` parameter.

    Arguments
    ---------
    filename : str
        Input filename.
    unexpected_attr : {'print' (default), 'error', 'quiet'}
        Behaviour if a PubMed field is found in the input file that is not
        supported (i.e., is not an attribute of `SingleRec`).

        'print': prints a message to standard output and continues
        'quiet': continues without printing a message to standard output
        'error': throws a `ValueError()` exception

    Returns
    -------
    A data frame

    Trademark Notice
    ----------------
    The PubMed wordmark is a registered trademark of the U.S. Department of
    Health and Human Services. This software is not endorsed by or affiliated
    with the trademark holders.
    '''
    # NB: need to use engine='python', as encountered buffer
    #  overflow errors on large file(s) with default engine
    df = pd.read_csv(filename, sep='\t', na_filter=False, quoting=3,
                 names=['line'], engine='python')
    output_list = []
    one_rec = SingleRec()
    lastattr = ''
    ignore_attr = ['CTDT']
    for line_index, line in enumerate(df['line']):
        if len(line) > 0:
            #print(line)
            if (len(line) < 5
                or (line[4] != '-' and line[4] != ' ')):
                raise ValueError(f'{filename}: Line {line_index}: not valid: '
                                 f'{line}')
            elif line[0:5] == 'PMID-':
                #print(f'{line_index}: Branch 1: {len(output_list)=}')
                if line_index > 0: output_list.append(copy.deepcopy(one_rec))
                one_rec.reset()
                setattr(one_rec, 'PMID', line[6:])
                lastattr = 'PMID'
            elif line[0:5] == '     ':
                #print(f'{line_index}: Branch 2: {lastattr=}')
                setattr(one_rec, lastattr,
                        getattr(one_rec, lastattr) + line[6:])
            else:
                #print(f'{line_index} Branch 3')
                lastattr = line[0:4].strip()
                if lastattr in ignore_attr: continue
                if not hasattr(one_rec, lastattr):
                    if unexpected_attr == 'error':
                        raise ValueError(f'{filename}: Line {line_index}: '
                                     f'unexpected attribute: {lastattr}')
                    elif unexpected_attr == 'quiet':
                        continue
                    elif unexpected_attr == 'print':
                        print(f'{filename}: Line {line_index}: '
                              f'unexpected attribute: {lastattr}')
                        continue
                currval = getattr(one_rec, lastattr)
                if currval != '':
                    setattr(one_rec, lastattr, currval + '; ' + line[6:])
                else:
                    setattr(one_rec, lastattr, line[6:])
    output_list.append(copy.deepcopy(one_rec))
    df = pd.DataFrame(output_list)
    df.set_index('PMID')
    return df

def df_to_txt(df: pd.DataFrame, filename: str,
              start_cols: Optional[list[str]]  = None,
              add_other_cols: bool = False) -> None:
    '''Write data frame to tab-delimited text file.

    Arguments
    ---------
    df : pandas.DataFrame
    filename : str
        Output filename.
    start_cols : list[str], optional
        List of column names to write first in the output.
    add_other_cols : boolean (default = False)
        If True, columns in data frame that are not in `start_cols` are
        also written to the output file.

    Returns
    -------
    None
    '''
    if start_cols is None:
        start_cols = []
    if add_other_cols:
        new_order = (start_cols
                    + [ x for x in df.columns if not x in start_cols ])
    else:
        new_order = start_cols
    if 'PMID' not in new_order:
        print('WARNING: df_to_txt: PMID field not requested in output')
    df_out = df[ new_order ]
    df_out.to_csv(filename, sep='\t', index=False, quoting=3, header=True)

def txt_to_df(filename: str) -> pd.DataFrame:
    '''Read a tab-delimited text file with no quoting into a data frame.
    '''
    df = pd.read_csv(filename, sep='\t', na_filter=False, quoting=3, dtype=str)
    df.set_index('PMID')
    return df

def merge_to_df(df: pd.DataFrame, filename: str,
                 tag: Optional[str], how: str = 'outer') -> pd.DataFrame:
    '''Merge PubMed output onto existing data frame.

    Arguments
    ---------
    df : pandas.DataFrame, optional
        Data frame that is one record per PubMed entry.
    filename : str
        File with PubMed-style output
    tag : str, optional
        Create a new variable with name of `tag` that takes value 'Y' if
        the record was in the `filename` parameter, and '' otherwise.
    how : str
        Passed to `df.merge()` when the merge is performed.

    Returns
    -------
    A data frame that is one record per PubMed entry that merges the
    PubMed entries from `filename` with the input data frame, and
    optionally adds the `tag` variable.

    Trademark Notice
    ----------------
    The PubMed wordmark is a registered trademark of the U.S. Department of
    Health and Human Services. This software is not endorsed by or affiliated
    with the trademark holders.
    '''
    update_df = pubmed_to_df(filename)
    merged_df = df.merge(update_df, how=how, validate='1:1', indicator=True)
    if tag:
        merged_df[tag] = np.where(merged_df['_merge'] != 'left_only',
                                  'Y', '')
    return merged_df.drop(columns=['_merge'])
