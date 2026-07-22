# GitHub Upload Guide — Windows PowerShell

## Option A: Upload through the GitHub website

1. Sign in to GitHub.
2. Select **New repository**.
3. Repository name:

   `mokhles-group-hr-analytics-bd-fy2025`

4. Do not initialise the repository with another README, licence or `.gitignore`.
5. Create the repository.
6. Extract the GitHub-ready ZIP.
7. Open the extracted folder.
8. Drag the folder contents into GitHub's **uploading an existing file** area.
9. Commit the files.

This method is suitable when the browser accepts the number and size of files.

## Option B: Upload through Git and PowerShell

Open PowerShell inside the extracted repository folder.

### 1. Verify Git

```powershell
git --version
```

### 2. Initialise the repository

```powershell
git init
git branch -M main
```

### 3. Add the files

```powershell
git add .
```

### 4. Create the first commit

```powershell
git commit -m "Initial release: Mokhles Group HR Analytics Demo 2025"
```

### 5. Connect the GitHub repository

Replace `<your-username>` when necessary:

```powershell
git remote add origin https://github.com/samusa099/mokhles-group-hr-analytics-bd-fy2025.git
```

### 6. Push

```powershell
git push -u origin main
```

## Validate before pushing

```powershell
py scripts\validate_repository.py
```

## Configure the GitHub About section

Copy the repository description, website and topics from:

`docs/GITHUB_ABOUT.md`
