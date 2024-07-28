<div align="center">
  <img src="https://github.com/AntoinePinto/easyenvi/blob/master/img/logo.png?raw=true"
  raw=true" alt="drawing" width="400"/>><br>
</div>

# Easy environment : easy-to-use Python environment management toolkit

**Easy Environment** is a Python tool that provides **easy-to-use functionality for managing files and data in different environments.** It offers a class that simplifies file operations on the local disk and cloud services such as Google Cloud (Google Cloud Storage and Big Query) or SharePoint.

## Features

* **Multi-format loading and saving**: Load and save files in various formats with one command line
  * **Default supported formats**: csv, docx, jpg, json, md, parquet, pdf, pickle, png, pptx, sql, toml, txt, xlsx, xml, yaml, yml
  * **Unsupported formats**: Customisable. See [Customise supported formats](https://antoinepinto.gitbook.io/easyenvi/extra/customise-supported-formats).
* **Multi-environment management**:
  * **Local disk**: Loading/saving and management.
  * **Google Cloud Storage**: Loading/saving and management.
  * **Big Query**: Append, write, and run queries on Big Query tables.
  * **SharePoint**: Download, upload, and manage files on SharePoint.

<p align="center">
  <img src="https://github.com/AntoinePinto/easyenvi/blob/master/img/table_support.png?raw=true" alt="drawing" width="800"/>
</p>

Start by installing `easyenvi` :

```python
pip install easyenvi
```

## Multi-format loading and saving

Load or save a large variety of format : csv, docx, jpg, json, md, parquet, pdf, pickle, png, pptx, sql, toml, txt, xlsx, xml, yaml, yml

```python
from easyenvi import file

secrets = file.load('my_path/secrets.toml')
config = file.load('my_path/config.json')
query = file.load('my_path/titanic.sql')

file.save(df, 'my_path/titanic.csv')
file.save(df, 'my_path/my_dict.parquet')
file.save(my_dict, 'my_path/my_dict.pickle')
```

## Multi-environment management

To use Easy Environment, create an instance of the `EasyEnvironment` class. All the parameters in the `EasyEnvironment` class are optional: it depends on which environment you need to access.

```python
from easyenvi import EasyEnvironment

envi = EasyEnvironment(
  local_path="", # Optional

  gcloud_project_id="your-project-id", # Optional
  gcloud_credential_path="path/to/credentials.json", # Optional
  GCS_path="gs://your-bucket-name/", # Optional

  sharepoint_site_url="https://{tenant}.sharepoint.com/sites/{site}", # Optional
  sharepoint_username="your-username", # Optional
  sharepoint_user_password="your-password" # Optional
                  )
```

Specifying certain parameters means certain dependencies: 
* For using **local operation**, `local_path` is the path from which local operations should be executed - specify an empty string if you want to use the current directory.
* For using **Google Cloud**, it is necessary to specify the project ID, the path to a credential .json file, and, in case of interaction with Google Cloud Storage, the path to the GCS folder (see [Google Cloud Initialisation](https://antoinepinto.gitbook.io/easyenvi/google-cloud-environment/google-cloud-initialisation)). 
* For using **SharePoint**, it is necessary to specify the SharePoint site to interact with, as well as authentication credentials: either the client_id/client_secret pair or the username/user_password pair (see [SharePoint Initialisation](https://antoinepinto.gitbook.io/easyenvi/sharepoint-environment/sharepoint-initialisation)).

## Examples of use

### Local features

```python
# Load any file format
my_dict = envi.local.load(path='inputs/my_dictionnary.pickle')
my_logo = envi.local.load(path='inputs/my_logo.png')
dataset = envi.local.load(path='inputs/dataset.csv')

# Save any file format
envi.local.save(obj=my_dict, path='outputs/my_dictionnary.pickle')
envi.local.save(obj=my_logo, path='outputs/my_logo.png')
envi.local.save(obj=dataset, path='outputs/dataset.csv')
```

### Google Cloud Storage features

```python
# Load any file format
my_dict = envi.gcloud.GCS.load(path='inputs/my_dictionnary.pickle')
my_logo = envi.gcloud.GCS.load(path='inputs/my_logo.png')
dataset = envi.gcloud.GCS.load(path='inputs/dataset.csv')

# Save any file format
envi.gcloud.GCS.save(obj=my_dict, path='outputs/my_dictionnary.pickle')
envi.gcloud.GCS.save(obj=my_logo, path='outputs/my_logo.png')
envi.gcloud.GCS.save(obj=dataset, path='outputs/dataset.csv')
```

### Big Query features

```python
df = pd.DataFrame(data={'age': [21, 52, 30], 'wage': [12, 17, 11]})

# Create a new table
envi.gcloud.BQ.write(dataset, 'mydata.mytable')

# Append an existing table
envi.gcloud.BQ.append(dataset, 'mydata.mytable')

# Run queries
query = """
SELECT *
FROM mydata.mytable
WHERE age < 40
"""

new_dataset = envi.gcloud.BQ.query(query).to_dataframe()
```

### SharePoint features

```python
# Download a file
envi.sharepoint.download(
  input_path="/Document partages/sharepoint_folder/my_file.txt",
  output_path="local_folder/my_file.txt"
  )
                        
# Upload a file
envi.sharepoint.upload(
  input_path="local_folder/my_file.txt",
  output_path="Document partages/folder/my_file.txt"
  )
                      
# List files
envi.sharepoint.list_files(folder="local_folder")
```

## Documentation

The documentation is available here : [Easy Environment - Documentation](https://antoinepinto.gitbook.io/easyenvi/)

## Future Improvements

Future releases of Easy Environment will include support for additional cloud storage providers, including Amazon Web Services (AWS) and Microsoft Azure.