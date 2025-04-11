Set-Location C:\Users\wille\OneDrive\GitHub\WillemGardner.github.io
python .\getjobnews.py
git add .
git commit -m "update: $(Get-Date -Format "dd-mm-yyyy hh:mm:ss")"
git push -u origin main
Write-Output "WillemGardner.github.io updated at $(Get-Date -Format "dd-mm-yyyy hh:mm:ss")"