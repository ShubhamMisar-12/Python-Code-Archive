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
        datetimeObj = datetime.strptime(entries[2], '%Y-%m-%d %H:%M:%S.%f')
        if datetimeObj.month not in month_dic.keys():
            month_dic[datetimeObj.month] = 1
        else:
            month_dic[datetimeObj.month] = month_dic[datetimeObj.month] + 1
    month_sorted= sorted(month_dic, key = lambda month: -month_dic[month])
    month_names = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 
              10:'October' , 11:'November', 12:'December'}
    header = ['AdmissionMonth', 'AdmissionCount']
    lines = []
    for month in month_sorted:
        lines.append([month_names[month], month_dic[month]])
    import csv
    with open('ex1.tsv', 'w', newline='') as f:
        #csv writer to write in tsv file
        tsv_writer = csv.writer(f, delimiter='\t')
        #write header in tsv file
        tsv_writer.writerow(header)
        #write rows
        tsv_writer.writerows(lines)
        #close csv file
        f.close()
        pass

    # END SOLUTION


def ex2():
    """
    Repeat ex1 but add the Quarter column 
    This is the last SQL query on https://mkzia.github.io/eas503-notes/sql/sql_6_conditionals.html#conditionals
    Hint: https://stackoverflow.com/questions/60624571/sort-list-of-month-name-strings-in-ascending-order
    """

    # BEGIN SOLUTION
    pass
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
    pass
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
    pass
    # END SOLUTION
