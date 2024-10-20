import pandas as pd

employee_columns = [
    'ID', 'Name', 'Position', 'Department', 'Business Unit', 'Gender',
    'Ethnicity', 'Age', 'Hire Date', 'Salary', 'Bonus', 'Country', 'City', 'End Date'
]

def load_employee_data(file_path):
    try:
        return pd.read_csv(file_path, encoding='ISO-8859-1', names=employee_columns, header=None)
    except Exception as error:
        print(f"Error reading the CSV file: {error}")
        return None

def createCollection(p_collection_name):
    print(f"Collection '{p_collection_name}' created.")

def indexData(p_collection_name, p_exclude_column):
    indexed_info = employee_data.drop(columns=[p_exclude_column], errors='ignore')
    print(f"Indexed data into collection '{p_collection_name}', excluding column '{p_exclude_column}':")
    print(indexed_info)

def searchByColumn(p_collection_name, p_column_name, p_column_value):
    results = employee_data[employee_data[p_column_name] == p_column_value]
    print(f"Search results in '{p_collection_name}' for {p_column_name} = {p_column_value}:")
    print(results)

def getEmpCount(p_collection_name):
    count = len(employee_data)
    print(f"Employee Count in '{p_collection_name}': {count}")
    return count

def delEmpById(p_collection_name, p_employee_id):
    global employee_data
    employee_data = employee_data[employee_data.ID != p_employee_id]
    print(f"Employee with ID '{p_employee_id}' deleted from collection '{p_collection_name}'.")

def getDepFacet(p_collection_name):
    department_counts = employee_data['Department'].value_counts().reset_index().rename(columns={0: 'Count', 'index': 'Department'})
    print(f"Department facet for '{p_collection_name}':")
    print(department_counts)

employee_data = load_employee_data('Employee Sample Data 1.csv')
if employee_data is not None:
    v_nameCollection = 'Hash_Dharun'
    v_phoneCollection = 'Hash_1234' 

    # Create collections
    createCollection(v_nameCollection)
    createCollection(v_phoneCollection)

    # Get employee count
    getEmpCount(v_nameCollection)

    # Index data
    indexData(v_nameCollection, 'Department')
    indexData(v_phoneCollection, 'Gender')

    # Delete an employee by ID
    delEmpById(v_nameCollection, 'E02003')

    # Get employee count again
    getEmpCount(v_nameCollection)

    # Search by column
    searchByColumn(v_nameCollection, 'Department', 'IT')
    searchByColumn(v_nameCollection, 'Gender', 'Male')
    searchByColumn(v_phoneCollection, 'Department', 'IT')

    # Get department facets
    getDepFacet(v_nameCollection)
    getDepFacet(v_phoneCollection)
