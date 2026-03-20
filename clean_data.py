import pandas as pd

df =pd.read_csv("customers-100.csv")

print("Initial Data:\n")
print(df.head())
print(df.info())

df = df.drop_duplicates()
print("\nDuplicates:", df.duplicated().sum())


df = df.drop(columns=["Index"], errors='ignore')


df["Subscription Date"] = pd.to_datetime(df["Subscription Date"], errors="coerce")

print("\nAfter Date Conversion:\n")
print(df.info())


df["First Name"] = df["First Name"].str.strip().str.title()
df["Last Name"] = df["Last Name"].str.strip().str.title()
df["Country"] = df["Country"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()
df["Company"] = df["Company"].str.strip().str.title()
df["Email"] = df["Email"].str.strip().str.lower()

print("\nAfter Text Cleaning:\n")
print(df.head())

df.to_csv("cleaned_customer.csv", index=False)

print("\n File saved successfully!")