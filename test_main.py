import unittest
import pandas as pd
import main
import json
import shutil
import os

file_path = './output/data.json'

class TestMain(unittest.TestCase):
    
    def setUp(self):
        self.testData = main.read_csv('test.csv',',') 
        

    def test_readcsv(self):
        print(self.testData.head())
        self.assertEqual(self.testData.shape, (6, 12))
        self.assertEqual(self.testData['FirstName'].tolist(), ['Rebbecca', 'Stevie', 'Mariko', 'Gerardo', 'Mayra', 'Idella'])
        self.assertEqual(self.testData['LastName'].tolist(), ['Didio', 'Hallo', 'Stayer', 'Woodka', 'Bena', 'Scotland'])
        self.assertEqual(self.testData['Company'].tolist(), ['Brandt, Jonathan F Esq','Landrum Temporary Services', 'Inabinet, Macre Esq', 'Morris Downing & Sherred', 'Buelt, David L Esq', 'Artesian Ice & Cold Storage Co'])
        self.assertEqual(self.testData['BirthDate'].tolist(), [16031989, 17081985, 2061993, 14051992, 20081973, 30011982])
        self.assertEqual(self.testData['Salary'].tolist(), [4949.2034, 64558.5195, 539508.372, 293515.5065, 395121.2553, 573376.9549])
        self.assertEqual(self.testData['Address'].tolist(), ['171 E 24th St', '22222 Acoma St', '534 Schoenborn St #51', '69206 Jackson Ave', '808 Glen Cove Ave', '373 Lafayette St'])
        self.assertEqual(self.testData['City'].tolist(), ['Leith', 'Proston', 'Hamel', 'Talmalmo', 'Lane Cove', 'Cartmeticup'])
        self.assertEqual(self.testData['State'].tolist(), ['TAS', 'QLD', 'WA', 'NSW', 'NSW', 'WA'])
        self.assertEqual(self.testData['Post'].tolist(), ['7315', '4613', '6215', '2640', '1595', '6316'])
        self.assertEqual(self.testData['Phone'].tolist(), ['0381749123', '0799973366', '0855589019', '0260444682', '0214556085','0878681355'])
        self.assertEqual(self.testData['Mobile'].tolist(), ['0458665290', '0497622620', '0427885282', '0443795912', '0453666885', '0451966921'])
        self.assertEqual(self.testData['Email'].tolist(), ['rebbecca.didio@didio.com.au', 'stevie.hallo@hotmail.com', 'mariko_stayer@hotmail.com', 'gerardo_woodka@hotmail.com', 'mayra.bena@gmail.com', 'idella@hotmail.com'])

    def test_transformdata(self):
        self.tranData=main.transform_data(self.testData)
        print(self.tranData['BirthDate'])
        print(self.tranData["SalaryBucket"])
        # self.assertEqual(self.tranData.shape, (6, 12))
        self.assertEqual(self.tranData['FullName'].tolist(), ['Rebbecca Didio', 'Stevie Hallo', 'Mariko Stayer', 'Gerardo Woodka', 'Mayra Bena', 'Idella Scotland'])
        self.assertEqual(self.tranData['Age'].tolist(), [53, 53, 54, 53, 53, 53])
        self.assertEqual(self.tranData['Address'].tolist(), ['171 E 24th St, Leith TAS 7315', '22222 Acoma St, Proston QLD 4613', '534 Schoenborn St #51, Hamel WA 6215', '69206 Jackson Ave, Talmalmo NSW 2640', '808 Glen Cove Ave, Lane Cove NSW 1595', '373 Lafayette St, Cartmeticup WA 6316'])
        self.assertEqual(self.tranData['SalaryBucket'].to_list(), ['A', 'B', 'C', 'C', 'C', 'C'])

    def test_loaddata(self):
        self.tranData=main.transform_data(self.testData)
        main.load_data(self.tranData)
        if os.path.isfile(file_path):
            with open(file_path) as json_file:
                data = json.load(json_file)
                print("======data=====")
                print(data)
                print(len(data))
                self.assertEqual(data[0][-1], 'Rebbecca Didio')
                self.assertEqual(data[0]['Age'], 53)
                self.assertEqual(data[0]['Address'], '171 E 24th St, Leith TAS 7315')
                self.assertEqual(data[0]['Salary'], 4949.2034)
                self.assertEqual(data[0]['SalaryBucket'], 'A')

    def tearDown(self):
        if os.path.isfile(file_path):
            os.remove(file_path)
        # if os.path.isdir('./output'):
        #     shutil.rmtree('./output')
        return super().tearDown()
