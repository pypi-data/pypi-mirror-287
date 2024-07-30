# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:38:57 2023

@author: QianYang

Upversion 30Jul2024
"""
import os
from CRFChecklistFunc import getFormList,OutFile,OutFile_Docx

class CheckListCreator():
    def __init__(self):
        pass
    
    @staticmethod
    def Creator(acrf_path, bcrf_path,for_rave,out_path = None,projectName = None,aCRFWord = None,CRFWord = None):
        try:            
            CRF_List = ["aCRF File", "blank CRF File"]
            CRF_File_Path = [acrf_path,bcrf_path]
            page_List = []
            for path in CRF_File_Path:
                dic = getFormList(path,for_rave)
                page_List.append(dic)

            if len(page_List) == 2:
                if out_path:                  
                    if projectName:
                        CKLout_path = os.path.join(out_path, projectName + "_CheckList.xlsx")
                    else:
                        CKLout_path = os.path.join(out_path, "CheckList.xlsx") 
                    OutFile(CKLout_path,page_List[0], CRF_List[0],page_List[1], CRF_List[1])
                elif aCRFWord and CRFWord:
                    CRF_word_Path = [aCRFWord,CRFWord] 
                    OutFile_Docx(page_List[0], CRF_word_Path[0],page_List[1], CRF_word_Path[1])

        except Exception as e:
            raise Exception(f"Error Occurs: {e}")

        