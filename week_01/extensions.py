filename = input("File name: ").strip().lower()
if '.gif' in filename:
    print("image/gif")
elif '.png' in filename:
    print("image/png")
elif '.jpg' in filename:
    print("image/jpeg")
elif '.jpeg' in filename:
    print("image/jpeg")
elif '.pdf' in filename:
    print("application/pdf")
elif '.zip' in filename:
    print("application/zip")
elif '.txt' in filename:
    print("text/plain")
else:
    print("application/octet-stream")
