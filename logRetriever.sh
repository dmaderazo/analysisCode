#!/bin/bash 

## Dont forget to process out the first 9 lines or whatever it is. 
# This still needs to be done
# This works on the .log files.
#!/bin/bash
 
while getopts ":a:" opt; do
  case $opt in
    a)
     # echo "-a was triggered, Parameter: $OPTARG" >&2
     	echo $OPTARG
	 sed -n '9,$p' $OPTARG | grep -h "[[:alpha:]]*\-[[:alpha:]]*" | tr ' ' '\n' | grep -h "[[:alpha:]]*\-[[:alpha:]]*"

	;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

#grep -h "[[:alpha:]]*\-[[:alpha:]]*" $fileVar | tr ' ' '\n' | grep -h "[[:alpha:]]*\-[[:alpha:]]*"
