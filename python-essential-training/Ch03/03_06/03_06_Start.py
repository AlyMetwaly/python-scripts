# Tempfile Module
import tempfile
# Create a temporary file
temp_file = tempfile.TemporaryFile()
# Write to a temporary file
temp_file.write(b"Save this special number for me: 5678309")
temp_file.seek(0)
# Read the temporary file
print(temp_file.read())
# Close the temporary file
temp_file.close()
