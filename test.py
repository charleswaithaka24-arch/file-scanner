try:
         from pathlib import Path
         from collections import defaultdict
         direction=Path(input("input file path:"))
         files_by_ext=defaultdict(list)
         for current in direction.iterdir():
            if current.is_file():
               ext=current.suffix
               stats=current.stat()
               size =stats.st_size
               files_by_ext[ext].append((current.name,size))
              # print(current.name,size)
         print()
         print("Files by their extensions")
         for e, n in files_by_ext.items():
            print(e,)
            print(" ",n )
         total=sum(1 for folder in direction.iterdir() )
         print()
         print("TOTAL FILE SUMMARY")
         for ext,files in files_by_ext.items():
          largest_file=sorted(files,key=lambda x:x[1],reverse=True)
          top=largest_file[:5]
          print()
          print(ext)
          print("Largest files in each extension :",top)
         print("Total number of files :",total)

         print("Total file size :",direction.stat().st_size,"bytes")
         
except FileNotFoundError:
    print("Invalid file path")