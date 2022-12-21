import csv
def ex1():
    
    """
    Reproduce ex1.tsv from 'AdmissionsCorePopulatedTable.txt'
    https://mkzia.github.io/eas503-notes/sql/sql_6_conditionals.html#conditionals
    Separate the columns by a tab
    """

    # BEGIN SOLUTION
    data_lst = []
    with open('AdmissionsCorePopulatedTable.txt') as f:
        data = f.read()
    from datetime import datetime
    month_dic = {}
    header = None
    for line in data.strip().split("\n"):
        if header is None:
            header = line.split("\t")
            continue
        entries = line.split("\t")
        data_lst.append(entries)
        datep = datetime.strptime(entries[2], '%Y-%m-%d %H:%M:%S.%f')
        if datep.month not in month_dic.keys():
            month_dic[datep.month] = 1
        else:
            month_dic[datep.month] = month_dic[datep.month] + 1
    month_sorted= sorted(month_dic, key = lambda month: -month_dic[month])
    month_names = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 
              10:'October' , 11:'November', 12:'December'}
    header = ['AdmissionMonth', 'AdmissionCount']
    lines = []
    for month in month_sorted:
        lines.append([month_names[month], month_dic[month]])
    lines = sorted(lines, key = lambda x: (-x[1],x[0])) 
    with open('ex1.tsv', 'w', newline='') as f:
        tsv_writer = csv.writer(f, delimiter='\t')
        tsv_writer.writerow(header)
        tsv_writer.writerows(lines)
        
        

    # END SOLUTION


def ex2():
    """
    Repeat ex1 but add the Quarter column 
    This is the last SQL query on https://mkzia.github.io/eas503-notes/sql/sql_6_conditionals.html#conditionals
    Hint: https://stackoverflow.com/questions/60624571/sort-list-of-month-name-strings-in-ascending-order
    """

    # BEGIN SOLUTION
    import csv
    data_lst = []
    with open('AdmissionsCorePopulatedTable.txt') as f:
        data = f.read()
    from datetime import datetime
    month_dic = {}
    header = None
    for line in data.strip().split("\n"):
        if header is None:
            header = line.split("\t")
            continue
        entries = line.split("\t")
        data_lst.append(entries)
        datetimeObj = datetime.strptime(entries[2], '%Y-%m-%d %H:%M:%S.%f')
        if datetimeObj.month not in month_dic.keys():
            month_dic[datetimeObj.month] = 1
        else:
            month_dic[datetimeObj.month] = month_dic[datetimeObj.month] + 1
    month_names = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 
              10:'October' , 11:'November', 12:'December'}
    Quater = {1: 'Q1', 2: 'Q1', 3: 'Q1', 4: 'Q2', 5: 'Q2', 6:'Q2', 7: 'Q3', 8:'Q3', 9: 'Q3', 10: 'Q4', 11: 'Q4', 12:'Q4'}
    header = ['Quarter','AdmissionMonth', 'AdmissionCount']
    lines = []
    for i in range(1,13):
        lines.append([Quater[i], month_names[i], month_dic[i]])
    

    with open('ex2.tsv', 'w', newline='') as f:
        tsv_writer = csv.writer(f, delimiter='\t')
        tsv_writer.writerow(header)
        tsv_writer.writerows(lines)
        
        

    # END SOLUTION


def ex3():
    """
    Reproduce 
    SELECT
        LabsCorePopulatedTable.PatientID,
        PatientCorePopulatedTable.PatientGender,
        LabName,
        LabValue,
        LabUnits,
        CASE
            WHEN PatientCorePopulatedTable.PatientGender = 'Male'
            AND LabValue BETWEEN 0.7
            AND 1.3 THEN 'Normal'
            WHEN PatientCorePopulatedTable.PatientGender = 'Female'
            AND LabValue BETWEEN 0.6
            AND 1.1 THEN 'Normal'
            ELSE 'Out of Range'
        END Interpretation
    FROM
        LabsCorePopulatedTable
        JOIN PatientCorePopulatedTable ON PatientCorePopulatedTable.PatientID = LabsCorePopulatedTable.PatientID
    WHERE
        LabName = 'METABOLIC: CREATININE'
    ORDER BY
        - LabValue

    using PatientCorePopulatedTable.txt and LabsCorePopulatedTable

    **** ADD  LabDateTime
    **** SORT BY Patient ID and then LabDateTime in ascending order 
    """
    # BEGIN SOLUTION
    with open('PatientCorePopulatedTable.txt') as f:
        data = f.read()
    patient = {}
    header_patient = None
    for line in data.strip().split("\n"):
        if not line.strip():
            continue
        if header_patient is None:
            header_patient = line.split("\t")
            continue
        clns = line.split("\t")
        patient[clns[0]] = clns[1:]
    
    with open('LabsCorePopulatedTable.txt') as f:
        data = f.read()
    
    Labs = []
    header_lab = None
    for line in data.strip().split("\n"):
        if not line.strip():
            continue
        if header_lab is None:
            header_lab = line.split("\t")
            continue
        clns = line.split("\t")
        if clns[2] == 'METABOLIC: CREATININE':
            Labs.append(clns)

    from datetime import datetime
    res = []
    for l in Labs:
        if l[0] in patient.keys():
            patient[l[0]]
            if patient[l[0]][0] == 'Male':
                if 0.7 <= float(l[3]) <= 1.3:
                    res.append([l[0], patient[l[0]][0], l[2], l[3], l[4], l[5] , 'Normal'])
                else:
                    res.append([l[0], patient[l[0]][0], l[2], l[3], l[4], l[5], 'Out of Range'])
            elif patient[l[0]][0] == 'Female':
                if 0.6 <= float(l[3]) <= 1.1:
                    res.append([l[0], patient[l[0]][0], l[2], l[3], l[4], l[5], 'Normal'])
                else:
                    res.append([l[0], patient[l[0]][0], l[2], l[3], l[4], l[5], 'Out of Range'])

    res = sorted(res, key = lambda x: (x[0], datetime.strptime(x[5], '%Y-%m-%d %H:%M:%S.%f')) )     

    header_res = ['PatientID','PatientGender', 'LabName','LabValue','LabUnits','LabDateTime', 'Interpretation']

    import csv

    with open('ex3.tsv', 'w', newline='') as f:
        tsv_writer = csv.writer(f, delimiter='\t')
        tsv_writer.writerow(header_res)
        tsv_writer.writerows(res)
              
                    

   
    # END SOLUTION


def ex4():
    """
    Reproduce this
    WITH AGE AS (
        SELECT 
            PATIENTID,
            ROUND((JULIANDAY('NOW') - JULIANDAY(PATIENTDATEOFBIRTH))/365.25) AGE
        FROM 
            PATIENTCOREPOPULATEDTABLE
    )
    SELECT 
        CASE 
            WHEN AGE < 18 THEN 'YOUTH'
            WHEN AGE BETWEEN 18 AND 35 THEN 'YOUNG ADULT'
            WHEN AGE BETWEEN 36 AND 55 THEN 'ADULT'
            WHEN AGE >= 56 THEN 'SENIOR'
        END AGE_RANGE,
        COUNT(*) AGE_RANGE_COUNT
    FROM 
        AGE
    GROUP BY AGE_RANGE

    
    ORDER BY AGE

    ****** VERY IMPORTANT: Use the Date: 2022-12-11 as today's date!!!! VERY IMPORTANT otherwise your result will change everyday!
    ****** VERY IMPORTANT divide the number of days by 365.25; to get age do math.floor(delta.days/365.25), where delta days is now-dob

    """
    # BEGIN SOLUTION
    from datetime import datetime

    with open('PatientCorePopulatedTable.txt') as f:
        data = f.read()
        
    p_ages = {}
    header_patient = None
    for line in data.strip().split("\n"):
        if not line.strip():
            continue
        if header_patient is None:
            header_patient = line.split("\t")
            continue
            
        clns = line.split("\t")
        
        str_d1 = '2022-12-11'
        str_d2 = clns[2]

        d1 = datetime.strptime(str_d1, "%Y-%m-%d")
        d2 = datetime.strptime(str_d2.split(" ")[0], "%Y-%m-%d")
        age = round((d1 - d2).days/365.25)
        if age < 18:
            per_age = "YOUTH"
        elif 18 <= age <= 36:
            per_age = "YOUNG ADULT"
        elif 36 < age <= 55:
            per_age = "ADULT"
        elif age >= 56:
            
            per_age = "SENIOR"
            
        if per_age not in p_ages.keys():
            p_ages[per_age] = 1
        else:
            p_ages[per_age] = p_ages[per_age] + 1
            
    

    age_strf= list(map(lambda x: [x, p_ages[x]], sorted(p_ages, key = lambda x: p_ages[x] ) ))
    header_strf = ['AGE_RANGE','AGE_RANGE_COUNT']

    import csv
    with open('ex4.tsv', 'w', newline='') as f:
        tsv_writer = csv.writer(f, delimiter='\t')
        tsv_writer.writerow(header_strf)
        tsv_writer.writerows(age_strf)
        
    # END SOLUTION
