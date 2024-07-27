import pandas as pd
import numpy as np
import warnings
import re

warnings.simplefilter('ignore')

class QC_Check:

    """
    This module is for generalized QC check on any project data including:
        -> PROMIS \n
        -> NAFLD \n
        -> DM \n
        -> PGR \n
        -> HF \n
        -> STROKE \n
    
    Checks included in this module are:
        -> Age limits > 95 or <18 \n
        -> Gender check (with respect to name) \n
        -> Women History check \n
        -> Medical History check \n
        -> Case & Control check (with respect to phenotype code) \n
        -> Family History check

    Note:
    ----------
        This module rename columns of data set from phenotype data dictionary.
    """
    

    # Constructor
    def __init__(self, dataframe: pd.DataFrame, project_id: str) -> None:
        """
        The class must be initiated with a pandas.DataFrame object of project data along with project ID

        Parameters
        ----------
        dataframe: pd.DataFrame object
        project_id: str (PROMIS, NAFLD, DM, PGR, STROKE)

        Return
        ----------
        return: None

        """
        self.dataframe = dataframe
        self.project_id = project_id

        if project_id == "PROMIS":
            gid = 1562895443
        elif project_id == "NAFLD":
            gid = 374727569
        elif project_id == "DM":
            gid = 663638861
        elif project_id == "PGR":
            gid = 10985616
        elif project_id == "HF":
            gid = 156158364
        elif project_id == "STROKE":
            gid = 834864365
        else:
            raise Exception("Kindly enter a valid project ID: PROMIS, NAFLD, DM, HF or PGR")
        #skedits: add the google sheet id link as input parameter
        """
        # Response:
            * How will we handle the GID if we make it as a user input?
        """            
        project_dictionary_link = f'https://docs.google.com/spreadsheets/d/1Fa6K_e7fRjEMdsBw6TzeMaC3oqo-cL568fuJfCdBoMA/export?format=csv&gid={gid}' 
        
        phenotype_coding_sheet_link = r"https://docs.google.com/spreadsheets/d/1Fa6K_e7fRjEMdsBw6TzeMaC3oqo-cL568fuJfCdBoMA/export?format=csv&gid=0"

        self.phenotype_coding_sheet = pd.read_csv(phenotype_coding_sheet_link)

        self.phenotype_coding_sheet['phenotype'] = self.phenotype_coding_sheet['phenotype'].str.upper().str.strip().str.replace("-", "").str.replace("  ", " ").str.replace("  ", " ")
        self.phenotype_coding_sheet['disease_status'] = self.phenotype_coding_sheet['disease_status'].str.upper().str.strip().str.replace("-", "").str.replace("  ", " ").str.replace("  ", " ")
        self.phenotype_coding_sheet.drop_duplicates(subset='center_alpha', keep='last', inplace=True)

        self.dataframe['center_alpha'] = self.dataframe['study_id'].apply(self.__get_center_alpha)

        self.project_dictionary = pd.read_csv(project_dictionary_link)
        self.project_dictionary = self.project_dictionary[self.project_dictionary['column_name'].notna()]

        project_dictionary = dict(
            zip(
                self.project_dictionary['entry1_header'].to_list(),
                self.project_dictionary['column_name'].to_list()
            )
        )

        self.dataframe.rename(columns=project_dictionary, inplace=True)
        for i in self.phenotype_coding_sheet.columns.to_list():
            self.phenotype_coding_sheet[i] = self.phenotype_coding_sheet[i].apply(lambda x: str(x).upper())

    def __get_center_alpha(self, x: str) -> any:
        try:
            return re.findall('[A-z]+', str(x).strip())[0]
        except:
            return None
        
    def get_float(self, x):
        try:
            return float(x)
        except:
            return None
    
    #skedits check for duplicates
    # -same id present twice
    # -
    def age_check(self, min_age = 15, max_age = 95) -> pd.DataFrame:
        """
        This function checks if the age is greater than 95 or less than 18.
    
        Parameters
        ----------
        None

        Return
        ----------
        return: pd.DataFrame object of records which have out of bounds age.
        """
        return self.dataframe[
            (self.dataframe['age'] > max_age) #skedits
            |
            (self.dataframe['age'] < min_age) #skedits
            |
            (self.dataframe.duplicated(subset="study_id", keep=False))
        ][['study_id', 'name', 'age']].reset_index(drop=True)
    
    #check with QC dashboard and sample recieving sheet is missing
    def gender_check(self, gender: str) -> pd.DataFrame:
        """
        This function checks if the gender is not correlating with the participant's name.

        Parameters
        ----------
        gender: str (male, female)
        
        Return
        ----------
        return: pd.DataFrame object of records which have non-correlating gender with respect to name.
        """

        gender_check_female = ['BIBI', 'MRS','BANO','W/O','D/O','MISS','MS','BB']
        gender_check_male = ['S/O' , 'MR']

        if self.project_id == "STROKE":
            # merge first_name and last_name
            self.dataframe['name'] = self.dataframe['first_name'] + ' ' + self.dataframe['family_name']

        
        gender_data = self.dataframe[['study_id','name','gender']]

        if gender == "male":

            gender_data['result'] = gender_data['name'].apply(
                lambda x : ','.join(
                    [item for item in str(x).split() if item.upper() in gender_check_male]
                )
            )

            return gender_data[
                (gender_data['result'].isin(gender_check_male))
                &
                (gender_data['gender'] == 2)
            ].reset_index(drop=True)
        
        elif gender == "female":

            gender_data['result'] = gender_data['name'].apply(
                lambda x : ','.join(
                    [item for item in str(x).split() if item.upper() in gender_check_female]
                )
            )

            return gender_data[
                (gender_data['result'].isin(gender_check_female))
                &
                (gender_data['gender'] == 1)
            ].reset_index(drop=True)
    
    
    def women_history_check(self) -> pd.DataFrame:
        """
        This function if any of the womens history columns are filled for males

        Parameters
        ----------
        None

        Return
        ----------
        return: pd.DataFrame object of records of male participants having female history records.
        """

        # for STROKE project
        if self.project_id == "STROKE":
            return self.dataframe[self.dataframe['gender'] == 1][
            (self.dataframe['subject_menstrual_state'] > 0)
            |
            (self.dataframe['subject_menstruation_last_12_months'] > 0)
            |
            (self.dataframe['subject_age_stop_menstruation'] > 0)
            |
            (self.dataframe['subject_reason_stop_menstruation'] > 0)
            |
            (self.dataframe['use_hormone_replacement_therapy'] > 0)

            ][[
                'study_id', 'name', 'gender', 'age',
                'status', 'subject_menstrual_state',
                'subject_menstruation_last_12_months',
                'subject_age_stop_menstruation',
                'subject_reason_stop_menstruation',
                'use_hormone_replacement_therapy'
            ]]
        
        # otherwise
        return self.dataframe[self.dataframe['gender'] == 1][
            (self.dataframe['subject_menstrual_state'] > 0)
            |
            (self.dataframe['subject_menstruation_last_12_months'] > 0)
            |
            (self.dataframe['subject_age_stop_menstruation'] > 0)
            |
            (self.dataframe['subject_reason_stop_menstruation'] > 0)
            |
            (self.dataframe['use_hormone_replacement_therapy'] > 0)
            |
            (self.dataframe['htn_pregnancy'] > 0)
            |
            (self.dataframe['dm_pregnancy'] > 0)
            |
            (self.dataframe['premature_birth'] > 0)
        ][[
            'study_id', 'name', 'gender', 'age',
            'status', 'subject_menstrual_state',
            'subject_menstruation_last_12_months',
            'subject_age_stop_menstruation',
            'subject_reason_stop_menstruation',
            'use_hormone_replacement_therapy',
            'htn_pregnancy', 'dm_pregnancy',
            'premature_birth'
            ]]
    
    """ We have paused this function since we applied this in family history check """
    # def medical_history_check(self) -> pd.DataFrame:
    #     """
    #     This function check if any of the disease age is greater than current age of participant.

    #     Parameters
    #     ----------
    #     None

    #     Return
    #     ----------
    #     return: pd.DataFrame object of records where disease age is greater than participant's age.
    #     """
    #     # generalized with loop and identify all columns with _age except family history
    #     medical_history_cols = [
    #         i for i in self.dataframe.columns.to_list()
    #             if "_age" in i
    #         and 
    #             "fh" not in i
    #         and
    #             "menstruation" not in i
    #         and
    #             "mother" not in i
    #         and
    #             "father" not in i
    #         and
    #             "sister" not in i
    #         and
    #             "brother" not in i
    #         and
    #             "son" not in i
    #         and
    #             "daughter" not in i
    #     ]

    #     temp = pd.DataFrame()

    #     for i in medical_history_cols:
    #         temp = pd.concat([temp, self.dataframe[self.dataframe[i] > self.dataframe['age']]], ignore_index=True)

    #     medical_history_cols.insert(0, "study_id")
    #     medical_history_cols.insert(1, "age")

    #     return temp[medical_history_cols]
    

    def pheno_code_check(self) -> pd.DataFrame:
        """
        This function check the status column with phenotype coding sheet.

        Parameters
        ----------
        None

        Return
        ----------
        return: pd.DataFrame object of records where the status column is different
                with respect to phenotype sheet.
        """

        self.phenotype_coding_sheet['status'] = 0

        self.phenotype_coding_sheet.loc[
            self.phenotype_coding_sheet["disease_status"].str.contains("CASE"),
            "status"
        ] = 1

        self.phenotype_coding_sheet.loc[
            self.phenotype_coding_sheet["disease_status"].str.contains("CONTROL"),
            "status"
        ] = 0

        checked_df = self.dataframe.merge(
            self.phenotype_coding_sheet,
            on=['center_alpha','status'],
            how='left',
            indicator=True
        )

        return checked_df[checked_df['_merge'] == 'left_only'][[
            'study_id','status','center_alpha'
        ]]


    # family history check including medical history
    #skedits: rename to medical_history  add check if diase_age <= 2 as well
    #add check if age < disease_age
    def medical_history_check(self) -> pd.DataFrame:  
        """
        This function is generalized with family history check in the update.
        It is now optimized and work properly.
    
        Parameters
        ----------
        None
    
        Return
        ----------
        return: pandas.DataFrame object with mismatched medical and faimly history columns
        """

        temp = self.dataframe.copy(deep=True)
        
        # generalized with loop
        selected_columns = []

        for col in temp.columns:
            if col.endswith("_age"):
                prefix = col[:-4]
                if prefix in temp.columns:
                    selected_columns.append(prefix)
                    selected_columns.append(col)

        temp.set_index('study_id', inplace=True)

        dis = temp[[i for i in selected_columns if '_age' not in i]]
        dis_age = temp[[i for i in selected_columns if '_age' in i]]
        dis.replace(0.0, np.nan, inplace=True)
        dis_age.replace(0.0, np.nan, inplace=True)

        mises = pd.concat(
            [
                dis[dis.notna().values != dis_age.notna().values].dropna(axis=0, how='all'), 
                dis_age[dis.notna().values != dis_age.notna().values].dropna(axis=0, how='all')
            ]
        )[selected_columns].reset_index()

        del temp
        #.set_index('study_id') skedits
        return pd.DataFrame(mises.groupby(by='study_id')[[i for i in mises.columns.to_list()[1:]]].last()).reset_index()
    

    def check_qc_status(self, disease_name: str="") -> pd.DataFrame:
        """
        This function check records with mismatched disease status.
    
        Parameters
        ----------
        disease_name: str (Only applicable in PGR checks) \n
            -> RHEUMATOID ARTHRITIS \n
            -> PSORIATIC ARTHRITIS \n
            -> SCLERODERMA \n
            -> ANKYLOSING SPONDYLITIS \n
            -> JUVENILE ARTHRITIC \n
            -> COPD \n
            -> ASTHMA \n
            -> DEMENTIA \n
            -> ACNE ROSACEA \n
            -> ALOPECIA AREATA \n
            -> ATOPIC DERMATITIS \n
            -> INFLAMMATORY ACNE (ACNE VULGARIS) \n
            -> MULTIPLE SCLEROSIS \n
            -> VITILIGO \n
            -> BREAST CANCER \n
            -> CERVICAL CANCER \n
            -> COLORECTAL CANCER \n
            -> LUNG CANCER \n
            -> KIDNEY CANCER \n
            -> PROSTATE CANCER \n
            -> OVARIAN CANCER \n
        Return
        ----------
        return: pandas.DataFrame object with mismatched disease status.
        """

        # PROMIS
        if self.project_id == "PROMIS":

            return self.dataframe[
                # remove checks for mi
                # add trop_positive_column
                (
                    (self.dataframe['status'] == 1)
                    &
                    (
                        (self.dataframe['troponin_positive'] != 1)
                        |
                        (self.dataframe['st_elevation'] != 1)
                    )
                )
                |
                (
                    (self.dataframe['status'] == 0)
                    &
                    (
                        (self.dataframe['troponin_positive'] == 1)
                        |
                        (self.dataframe['st_elevation'] == 1)
                    )
                )
            ][['study_id', 'status', 'mi', 'pre_mi', 'st_elevation', 'troponin_positive']]
        
        # NAFLD
        elif self.project_id == "NAFLD":

            return self.dataframe[
                (
                    (self.dataframe['status'] == 1)
                    &
                    # Add cap score too
                    (
                        (
                            (self.dataframe['cap_score'].isna())
                            |
                            (self.dataframe['cap_score'] < 238)
                        ) #skedit cap_score is null or cap_score < 238
                        &
                        (self.dataframe['fibroscan_capscore_mean'].isna())
                        &
                        (self.dataframe['ultrasound_report'].isna())
                        &
                        (self.dataframe['diagnosed_fatty_liver_disease'] != 1)
                    )
                )
                |
                (
                    (self.dataframe['status'] == 0)
                    &
                    (
                        (
                            (
                                (self.dataframe['fibroscan_capscore_mean'].notna())
                                |
                                (self.dataframe['cap_score'] > 238)
                            ) # add condition: cap_score > 238
                            &
                            (self.dataframe['fibroscan_capscore_mean'] != '0')
                        )
                        |
                        (
                            (self.dataframe['ultrasound_report'].notna())
                            &
                            (self.dataframe['ultrasound_report'] != '0')
                        )
                        |
                        (self.dataframe['diagnosed_fatty_liver_disease'] == 1)
                    )
                )
            ][['study_id','status','fibroscan_capscore_mean','ultrasound_report','diagnosed_fatty_liver_disease']]
        
        # DM
        elif self.project_id == "DM":

            return self.dataframe[
                (
                    (self.dataframe['dm'] == 1)
                    &
                    (self.dataframe['status'] != 1)
                )
                |
                (
                    (self.dataframe['dm_medicine'] == 1)
                    &
                    (self.dataframe['status'] != 1)
                )
                |
                (
                    (self.dataframe['dm_age'] > 0)
                    &
                    (self.dataframe['status'] != 1)
                )
            ][['study_id', 'status', 'dm', 'dm_age', 'dm_medicine']] #skedits check medicine names and see that insulin, metformin etc. are not being taken

        # STROKE
        elif self.project_id == "STROKE":

            return self.dataframe[
                    
                (
                    (
                        (self.dataframe['Computed_tomography'].notna())
                        |
                        (self.dataframe['Magnetic_resonance'].notna())
                    )      
                    &
                    (self.dataframe['status'] != 1)
                )
                |
                (
                    (
                        (self.dataframe['Computed_tomography'].isna())
                        &
                        (self.dataframe['Magnetic_resonance'].isna())
                    )      
                    &
                    (self.dataframe['status'] == 1)
                )
                
            ][[
                'study_id',
                'status',
                'Computed_tomography',
                'Magnetic_resonance'
            ]]
        
        # PGR
        elif self.project_id == "PGR":

            """
            PGR All cases:
                * Rheumatoid Arthritis 
                * Psoriatic Arthritis
                * Scleroderma
                * Ankylosing Spondylitis
                * Osteoarthritis
                * Juvenile Arthritis --leave
                * Ophthalmology
                * COPD / Asthma
                * CKD --> need biomarkers (egfr <= 90)
                * Parkinsons --leave
                * Dementia -- leave
                * Alzheimers --leave

            Cases done till now:
                * Rheumatoid Arthritis
                * Psoriatic Arthritis
                * Scleroderma
                * Ankylosing Spondylitis
                * Juvenile Arthritis
                * Ophthalmology
                * COPD / Asthma
                * Dementia
            """
            
            test_pheno = self.phenotype_coding_sheet[
                self.phenotype_coding_sheet['disease_status'].apply(
                    lambda x: True if disease_name in x.upper() else False
                )
            ]

            df = pd.merge(left=self.dataframe, right=test_pheno['center_alpha'], on='center_alpha', how='right')

            if disease_name == "RHEUMATOID ARTHRITIS":
                sdf = df[[
                    'morning_stiffness_acr',
                    'arthiritis_affects_acr',
                    'arthiritis_hand_joins_acr',
                    'arthiritis_symmetric_acr',
                    'rheumatoid_nodules_acr',
                    'rf_positive_acr',
                    'erosions_of_hand_foot_xray'
                ]] == 1

                df['acr_symptoms_count'] = sdf.sum(axis=1)

                return df[df['total_score_acr'].notna()][
                    
                    (
                        (df['acr_symptoms_count'] >= 4)
                        &
                        (df['status'] == 0)
                        &
                        (df['total_score_acr'] > 6)
                    )
                    |
                    (
                        (df['acr_symptoms_count'] < 4)
                        &
                        (df['status'] == 1)
                        &
                        (df['total_score_acr'] < 6)
                    )
                ][[
                    'study_id',
                    'status',
                    'morning_stiffness_acr',
                    'arthiritis_affects_acr',
                    'arthiritis_hand_joins_acr',
                    'arthiritis_symmetric_acr',
                    'rheumatoid_nodules_acr',
                    'rf_positive_acr',
                    'erosions_of_hand_foot_xray',
                    'total_score_acr',
                    'acr_symptoms_count'
                ]]
            
            elif disease_name == "PSORIATIC ARTHRITIS":

                return df[
                    
                    (
                        (df['caspar_total_score'] > 3)
                        &
                        (df['caspar_negative_rheumatoid_factor'] == 1)
                        &
                        (df['status'] != 1)
                    )
                    |
                    (
                        (df['caspar_total_score'] <= 3)
                        &
                        (df['caspar_negative_rheumatoid_factor'] != 1)
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'caspar_negative_rheumatoid_factor',
                    'caspar_total_score'
                ]]
            
            elif disease_name == "SCLERODERMA":

                return df[
                    
                    (
                        (df['total_score_sclerosis'] >= 9)
                        &
                        (df['status'] != 1)
                    )
                    |
                    (
                        (df['total_score_sclerosis'] < 9)
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'total_score_sclerosis'
                ]]
            
            elif disease_name == "ANKYLOSING SPONDYLITIS":

                sdf = df[[
                    "spa_features_arthiritis",
                    "spa_features_enthesitis",
                    "spa_features_dactylitis",
                    "spa_features_psoriasis",
                    "spa_features_elevated_crp"
                ]] == 1

                df['spa_features_count'] = sdf.sum(axis=1)
                return df[
                    ((
                        (df['low_back_pain_more_than_3_months'] == 1)
                        &
                        (df['back_pain_onset_before_45_years'] == 1)
                    )
                    &
                    (
                        (df['hlab27'] == 1)
                        |
                        (df['sacrolitis_xray'] == 1)
                        |
                        (df['active_inflammation_mri'] == 1)
                        |
                        (df['spa_features_count'] >= 2)
                    )
                    &
                    (df['status'] != 1))
                    |
                    ((
                        (df['low_back_pain_more_than_3_months'] != 1)
                        &
                        (df['back_pain_onset_before_45_years'] != 1)
                    )
                    &
                    (
                        (df['hlab27'] != 1)
                        |
                        (df['sacrolitis_xray'] != 1)
                        |
                        (df['active_inflammation_mri'] != 1)
                        |
                        (df['spa_features_count'] < 2)
                    )
                    &
                    (df['status'] == 1))

                ][[
                    'study_id',
                    'status',
                    'low_back_pain_more_than_3_months',
                    'back_pain_onset_before_45_years',
                    'hlab27',
                    'sacrolitis_xray',
                    'active_inflammation_mri',
                    "spa_features_arthiritis",
                    "spa_features_enthesitis",
                    "spa_features_dactylitis",
                    "spa_features_psoriasis",
                    "spa_features_elevated_crp",
                    "spa_features_count"
                ]]
            
            elif disease_name == "JUVENILE ARTHRITIC":

                return df[
                    
                    (
                        (df['acr_joint_inflammation'] == 1)       
                        &
                        (df['arc_patient_age_less_than_16'] == 1)
                        &
                        (df['acr_exclusion_infection'] == 1)
                        &
                        (df['status'] != 1)
                    )
                    |
                    (
                        (df['acr_joint_inflammation'] != 1)       
                        &
                        (df['arc_patient_age_less_than_16'] != 1)
                        &
                        (df['acr_exclusion_infection'] != 1)
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'acr_joint_inflammation',
                    'arc_patient_age_less_than_16',
                    'acr_exclusion_infection'
                ]]
            
            elif disease_name == "COPD":

                return df[
                    
                    (
                        (
                            (df['total_catscore'].notna())
                            |
                            (df['total_catscore'] > 0)
                        )      
                        &
                        (df['status'] != 1)
                    )
                    |
                    (
                        (
                            (df['total_catscore'].isna())
                            |
                            (df['total_catscore'] == 0)
                        )      
                        &
                        (df['status'] == 1)
                    )
                    
                ][[
                    'study_id',
                    'status',
                    'total_catscore'
                ]]

            

            elif disease_name == "ASTHMA":

                    return df[
                        
                        (
                            (
                                (df['total_actscore'].notna())
                                |
                                (df['total_actscore'] > 0)
                            )      
                            &
                            (df['status'] != 1)
                        )
                        |
                        (
                            (
                                (df['total_actscore'].isna())
                                |
                                (df['total_actscore'] == 0)
                            )      
                            &
                            (df['status'] == 1)
                        )
                        
                    ][[
                        'study_id',
                        'status',
                        'total_actscore'
                    ]]
            
            elif disease_name == "DEMENTIA": #leave out dementia

                    return df[
                        
                        (
                            (df['mmse_total_score'] < 25) 
                            &
                            (df['status'] != 1)
                        )
                        |
                        (
                            (df['mmse_total_score'] >= 25)     
                            &
                            (df['status'] == 1)
                        )
                        
                    ][[
                        'study_id',
                        'status',
                        'mmse_total_score'
                    ]]
            
            # __UPDATE__
            
            elif disease_name == 'ACNE ROSACEA':

                return df[
                    (
                        (df['acne_rosacea_exclusion_criteria'] != 1)
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['acne_diagnosis_age'].isna())
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'acne_rosacea_exclusion_criteria',
                    'acne_diagnosis_age'
                ]]
            
            elif disease_name == 'ALOPECIA AREATA':

                return df[
                    (
                        (df['alopecia_exclusion_criteria'] != 1)
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['alopecia_diagnosis_age'].isna())
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['distribution_patchy_hair_loss'] != 1)
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'alopecia_exclusion_criteria',
                    'alopecia_diagnosis_age',
                    'distribution_patchy_hair_loss'
                ]]
            
            elif disease_name == 'ATOPIC DERMATITIS':

                return df[
                    (
                        (df['atopic_dermatitis_exclusion_criteria'] != 1)
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['atopic_dermatitis_diagnosis_age'].isna())
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'atopic_dermatitis_exclusion_criteria',
                    'atopic_dermatitis_diagnosis_age'
                ]]
            
            elif disease_name == 'INFLAMMATORY ACNE':

                return df[
                    (
                        (df['acne_vulgaris_exclusion_criteria'] != 1)
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['acne_vulgaris_diagnosis_age'].isna())
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'acne_vulgaris_exclusion_criteria',
                    'acne_vulgaris_diagnosis_age'
                ]]
            
            elif disease_name == 'MULTIPLE SCLEROSIS':

                return df[
                    (
                        (df['mcdonald_criteria'] != 1)
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['mcdonald_diagnosis_age'].isna())
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'mcdonald_criteria',
                    'mcdonald_diagnosis_age'
                ]]
            
            elif disease_name == 'VITILIGO':

                return df[
                    (
                        (df['non_segmental_vitiligo'] != 1)
                        &
                        (df['non_segm_subtype'] != 1)
                        &
                        (df['segment_vitiligo'] != 1)
                        &
                        (df['segment_subtype'] != 1)
                        &
                        (df['mixed_nsv_sv'] != 1)
                        &
                        (df['nsv_sv_subtype'] != 1)
                        &
                        (df['unclassified'] != 1)
                        &
                        (df['unclassified_subtype'] != 1)
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['vitiligo_diagnosis_age'].isna())
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'non_segmental_vitiligo',
                    'non_segm_subtype',
                    'segment_vitiligo',
                    'segment_subtype',
                    'mixed_nsv_sv',
                    'nsv_sv_subtype',
                    'unclassified',
                    'unclassified_subtype',
                    'vitiligo_diagnosis_age'
                ]]
            
            elif disease_name == 'BREAST CANCER':

                return df[
                    (
                        (df['breast_cancer_diagnos_age'].isna())
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['breast_ultrasound'] != 1)
                        &
                        (df['two_low_dose_xray_breast'] != 1)
                        &
                        (df['biopsy'] != 1)
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'breast_cancer_diagnos_age',
                    'breast_ultrasound',
                    'two_low_dose_xray_breast',
                    'biopsy',
                ]]
            
            elif disease_name == 'CERVICAL CANCER':

                return df[
                    (
                        (df['cervical_cancer_diagnosis_age'].isna())
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['papanicolaou_finding'].isna())
                        &
                        (df['HPV_DNA_finding'].isna())
                        &
                        (df['cervical_biopsy_repots'].isna())
                        &
                        (df['colposcopy_finding'].isna())
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'papanicolaou_finding',
                    'HPV_DNA_finding',
                    'cervical_biopsy_repots',
                    'colposcopy_finding',
                ]]
            
            elif disease_name == 'COLORECTAL CANCER':
                return df[
                    (
                        (df['colorectal_carcinoma_diagnosis_age'].isna())
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['colorectal_staging'].isna())
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'colorectal_carcinoma_diagnosis_age',
                    'colorectal_staging'
                ]]
            
            elif disease_name == 'LUNG CANCER':
                return df[
                    (
                        (df['curative'].isna())
                        &
                        (df['curative_type'].isna())
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['intermediate_curative'].isna())
                        &
                        (df['intermediate_curative_type'].isna())
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['advance_palliative'].isna())
                        &
                        (df['advance_palliative_type'].isna())
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['limited_disease_curative'].isna())
                        &
                        (df['extensive_disease_palliative'].isna())
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'curative', 'curative_type',
                    'intermediate_curative',
                    'intermediate_curative_type',
                    'advance_palliative',
                    'advance_palliative_type',
                    'limited_disease_curative',
                    'extensive_disease_palliative'
                ]]
            
            elif disease_name == 'KIDNEY CANCER':
                return df[
                    (
                        (df['renal_cancer_diagnosis_age'].isna())
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['ct_report'].isna())
                        &
                        (df['mri_report'].isna())
                        &
                        (df['renal_biopsy_finding'].isna())
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'ct_report',
                    'mri_report',
                    'renal_biopsy_finding'
                ]]
            
            
            elif disease_name == 'PROSTATE CANCER':
                return df[
                    (
                        (df['prostrate_cancer_diagnosis_age'].isna())
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['prostrate_antigen_test'].isna())
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['transrectal_ultrasound'].isna())
                        &
                        (df['prostrate_biopsy'].isna())
                        &
                        (df['pet_ct'].isna())
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['localized_prostrate'].isna())
                        &
                        (df['localized_advanced'].isna())
                        &
                        (df['metastatic_prostrate'].isna())
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'prostrate_cancer_diagnosis_age',
                    'prostrate_antigen_test',
                    'transrectal_ultrasound',
                    'prostrate_biopsy',
                    'pet_ct',
                    'localized_prostrate',
                    'localized_advanced',
                    'metastatic_prostrate'
                ]]
            
            elif disease_name == 'OVARIAN CANCER':
                return df[
                    (
                        (df['ovarian_tumors_diagnosis_age'].isna())
                        &
                        (df['status'] == 1)
                    )
                    |
                    (
                        (df['ct_report'].isna())
                        &
                        (df['mri_report'].isna())
                        &
                        (df['pelvic_report'].isna())
                        &
                        (df['tissue_diagnosis_finding'].isna())
                        &
                        (df['status'] == 1)
                    )
                ][[
                    'study_id',
                    'status',
                    'ovarian_tumors_diagnosis_age',
                    'ct_report',
                    'mri_report',
                    'pelvic_report',
                    'tissue_diagnosis_finding',
                ]]


    def get_qc_IDs(self):

        """
        This function apply all of the QC checks we defined in this Promise QC file
        and give us all of the mis-informed IDs found during any of the defined checks.

        This function now excludes qc status function
        as that function requires specific project ID to filter the data first.

        On the other hand this function will now check the medical and family history checks.

        Parameters
        ----------
        None

        Return
        ----------
        return: pandas.DataFrame object including IDs found during any of the QC check.
        """
        return pd.concat(
            [
                self.gender_check('male'),
                self.gender_check('female'), 
                self.women_history_check(),
                self.medical_history_check(),
                # self.family_history_check(),
                self.pheno_code_check(),
                # self.check_qc_status(disease_name=disease_name)
            ]
        ).replace({"": np.nan}).groupby("study_id").first().reset_index()
        
        