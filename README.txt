Prerequisites:

Modules required : pip, requests, json(built-in module)

To check whether above modules already exists ? Type in the command line "pydoc modules | grep <module_name>" and hit enter (eg: pydoc modules | grep requests)
If you can see the module name listed in the output, then you can skip the appropriate step(s) mentioned below where the module already exists

Steps:

1) First make sure you are logged/switched as super user to have privileges to install the packages (Commands: sudo su, su <user_name> )
2) pip - installer to install python modules, hence place the get-pip.py in your present working directory(PWD).
3) If "pip" module not exists ? Type in the command line as "python get-pip.py" and hit enter, which will install you the "pip" module
4) If "requests" module not exists ? Type in the command line as "pip install requests" and hit enter, which will install you the "requests" module


Once the installation done, ALL SET!!

To run the CODE:

 Place the code file in your PWD, 
    syntax to run the code as below,
    
        To know the total number of samples available:
        python ebi_test.py --total_count

                   or 

        To know the sample name from the given accession:
        python ebi_test.py --acc  SAMD00000328

                   or 

        To know the accession from the given attribute:value pair
        python ebi_test.py --attr organism:Streptococcus+pyogenes strain:MTB313
       
If you could see all the results as expected, ALL DONE!!!
