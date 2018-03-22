import pyexcel

a_list_of_dictionaries = [
    {
        "title" : "hom nay",
        "link" : "https"
    },
    {
                "title" : "hom nay",
                "link" : "https"
    }
]
pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="test12.xlsx")
