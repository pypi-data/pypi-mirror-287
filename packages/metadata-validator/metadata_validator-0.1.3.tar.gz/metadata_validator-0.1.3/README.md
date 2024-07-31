### Metadata Validation Package
>
>****
>
>> #### About
>>
>> The metadata validation package is meant for the use of the Brain Image Library. The metadata dependencies match the required checkpoints for the submission of an Excel spreadsheet. The spreadsheet needs to match required criteria for a brain imagery dataset with supporting information.
>>
>> #### Instructions on Installation
>>
>> The steps to correctly install the package to a Linux system are:
>>
>> 1. Setup Virtual environment for package dependencies on command line Linux Interface within desired directory
>>
>>      * **$ python3 -m venv venv_for_package**
>>
>> 2. Activate Virtual Environment
>>
>>      * **$ source venv_for_package/bin/activate**
>> 3. Move into desired directory for package to pip install Metadata Validation Package
>>
>>      * **$ pip install metadata_validator**
>
> ****
>
>> #### Using Metadata Validation Package
>>
>> To start using the Metadata Validation package, the directory that the package was installed to has to be current directory path. The spreadsheet that is being checked will be located in this same directory as well for easy use of the package. The spreadsheet can also be placed in a different directory within the Linux system, but the first option is recommended.
>>
>> 1. Get to Python3 Shell Command Line
>>
>>      * **$ python3**
>>
>> 2. Import package from Linux directory to Python3 shell
>>
>>      * **>>> import metadata_validator**
>>
>> 3. Run function from package for metadata validation
>>
>>      * **>>> metadata_validator.outside_bil_check()**
>>
>>After running this command, the package will begin to operate and ask the user for an input of an absolute pathway to a excel spreadsheet
>>
>> 4. Give desired spreadsheet path
>>
>>      * Method 1: **>>> current_directory/spreadsheet.xlsx**
>>
>>      * Method 2: **>>> ~/path_to_spreadsheet/spreadsheet.xlsx**
>>
>> This will prompt a choice of a Ingest Method for different checks of different sheets within file.
>>
>> 5. Give Ingest Method
>>
>>      * **Choice of a number one through five**
>>
>>Once completed, the package will sift through different sheets within the spreadsheet checking metadata for valid inputs of information.
