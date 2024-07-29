import pandas
import random

SILENT_GEN = [1928, 1945]
BOOMERS_GEN = [1946, 1964]
X_GEN = [1965, 1980]
MILLENNIAL_GEN = [1981, 1996]
Z_GEN = [1997, 2012]
ALPHA_GEN = [2013, 2024]
class HyDi:
    def __init__(
            self,
            default_length=6,
            id_starting_namecode='I',
            id_male_namecode='M',
            id_female_namecode='F',
            id_other_namecode='O',
            id_general_agroup_sile='S',
            id_general_agroup_boom='B',
            id_general_agroup_x='X',
            id_general_agroup_mill='Y',
            id_general_agroup_z='Z',
            id_general_agroup_alph='A',
            df_file='./test_userids.csv',
            file_userid_column_label='userid',
            file_refer_column_label = 'refer_to'
    ):
        """
        HyDi is an over-simplified UserID generator.
        HyDi can generate UserIDs by itself and can also refer to an old UserID set by another platform.

        Useful Discord Bot Example:
        /warn IMZ-991823 'Swearing.'

        You don't have to rely on a username that can be changed or a big number that's hard to remember anymore.

        ONLY CSV EXPORT CURRENTLY SUPPORTED.
        :param default_length: - The UserID length (ONLY THE AUTO-GENERATED NUMBERS).
        :param id_starting_namecode: - The starting character/s of the UserID (IF NOT NEEDED SET TO '').
        :param id_male_namecode: - The character/s used in the UserID to quickly and easily identify male users.
        :param id_female_namecode: - The character/s used in the UserID to quickly and easily identify female users.
        :param id_other_namecode: - The character/s used in the UserID to quickly and easily identify users with no defined gender.
        :param id_general_agroup_sile: - The character/s used in the UserID to quickly and easily identify users from the Silent generation.
        :param id_general_agroup_boom: - The character/s used in the UserID to quickly and easily identify users from the Baby Boomers generation.
        :param id_general_agroup_x: - The character/s used in the UserID to quickly and easily identify users from the X generation.
        :param id_general_agroup_mill: - The character/s used in the UserID to quickly and easily identify users from the Millennial generation.
        :param id_general_agroup_z: - The character/s used in the UserID to quickly and easily identify users from the Z generation.
        :param id_general_agroup_alph: - The character/s used in the UserID to quickly and easily identify users from the Alpha generation.
        :param df_file: - The file used to pull and save data from/to (CSV ONLY CURRENTLY)
        :param file_userid_column_label: - The label under which the HyDi UserIDs will be saved.
        :param file_refer_column_label: - The label under which the platform-set/old UserIDs will be saved.
        :

        """

        self.id_starting_characters = id_starting_namecode
        self.default_length = default_length
        self.id_gender_namecodes= [id_male_namecode, id_female_namecode, id_other_namecode]
        self.id_general_age_groups = [id_general_agroup_sile, id_general_agroup_boom, id_general_agroup_x,
                                      id_general_agroup_mill, id_general_agroup_z, id_general_agroup_alph]
        self.df_file = df_file
        self.file_userid_label = file_userid_column_label
        self.file_refer_label = file_refer_column_label

        self.df_uids = pandas.read_csv(self.df_file)

    def gen(self, gender, b_year, refer_to=None):
        """
        Generates a HyDi UserID.
        :param gender: - User's gender (used in ID)
        :param b_year: - Birth year (determines the assigned generation)
        :param refer_to: - Refer to a platform-set/old UserID
        """

        id_gender_code = self._get_gender_code(gender)
        id_agegroup_code = self._get_age_group_code(b_year)

        uid = self._generate_unique_id(id_gender_code, id_agegroup_code)

        self._save_uid(uid, refer_to)

    def _get_gender_code(self, gender):
        """
        Returns the gender code based on the input.

        :param gender: - Gender of the user (M, F, or O).
        :return: - The corresponding gender code.
        """

        gender = gender.lower()
        if gender == "m":
            return self.id_gender_namecodes[0]
        elif gender == "f":
            return self.id_gender_namecodes[1]
        else:
            return self.id_gender_namecodes[2]

    def _get_age_group_code(self, b_year):
        """
        Returns the age group code based on the birth year.

        :param b_year: - Birth year of the user.
        :return: - The corresponding age group code.
        """

        if SILENT_GEN[0] <= b_year <= SILENT_GEN[1]:
            return self.id_general_age_groups[0]
        elif BOOMERS_GEN[0] <= b_year <= BOOMERS_GEN[1]:
            return self.id_general_age_groups[1]
        elif X_GEN[0] <= b_year <= X_GEN[1]:
            return self.id_general_age_groups[2]
        elif MILLENNIAL_GEN[0] <= b_year <= MILLENNIAL_GEN[1]:
            return self.id_general_age_groups[3]
        elif Z_GEN[0] <= b_year <= Z_GEN[1]:
            return self.id_general_age_groups[4]
        elif ALPHA_GEN[0] <= b_year <= ALPHA_GEN[1]:
            return self.id_general_age_groups[5]
        else:
            return 'u'

    def _generate_unique_id(self, id_gender_code, id_agegroup_code):
        """
        Generates a unique HyDi UserID.

        :param id_gender_code: - Gender namecode.
        :param id_agegroup_code: - Age group namecode.
        :return: - A unique HyDi UserID.
        """

        uid_already_exists = True
        while uid_already_exists:
            char_list = [self.id_starting_characters, id_gender_code, id_agegroup_code, '-']
            for _ in range(self.default_length):
                char_list.append(str(random.randint(0, 9)))
            uid = ''.join(char_list)

            if self.df_uids.isin([uid]).any().any():
                uid_already_exists = True
            else:
                uid_already_exists = False
        return uid

    def _save_uid(self, uid, refer_to):
        """
        Saves the generated UserID and reference ID to the CSV file.

        :param uid: - The generated HyDi UserID.
        :param refer_to: - The reference ID.
        """

        data = {self.file_userid_label: uid, self.file_refer_label: refer_to}
        self.df_uids = self.df_uids.append(data, ignore_index=True)
        self.df_uids.to_csv(self.df_file, index=False)