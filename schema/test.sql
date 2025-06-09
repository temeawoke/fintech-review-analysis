
import oracledb

# Only call this if you're trying to use Thick mode
try:
    oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_12")
    mode = "Thick mode (Instant Client)"
except Exception as e:
    mode = f"Thin mode (default) or Thick init failed: {e}"

conn = oracledb.connect(
    user="system",
    password="root",
    dsn="localhost/XEPDB1"
)

print("Connected:", conn.version)
print("Mode:", mode)
conn.close()
