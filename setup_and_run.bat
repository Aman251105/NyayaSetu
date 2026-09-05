@echo off
setlocal enabledelayedexpansion

:: ============================================================
::  NyayaSetu - One-Click Setup & Launch Script
::  Digital Justice & Undertrial Rehabilitation Platform
::
::  Usage:
::    setup_and_run.bat            -> Interactive Mode / Default Run
::    setup_and_run.bat --dev      -> Dual Server Dev Mode (Vite HMR + Django)
::    setup_and_run.bat --prod     -> Production Mode (Django serves built React UI)
::    setup_and_run.bat --backend  -> Backend API Only (http://127.0.0.1:8000/api/)
::    setup_and_run.bat --seed     -> Re-seed comprehensive demo database & exit
:: ============================================================

title NyayaSetu - Digital Justice Platform Launcher

set "ROOT=%~dp0"
if "%ROOT:~-1%"=="\" set "ROOT=%ROOT:~0,-1%"
set "PROJECT_DIR=%ROOT%"
set "BACKEND_DIR=%PROJECT_DIR%\backend"
set "FRONTEND_DIR=%PROJECT_DIR%\frontend"
set "VENV_DIR=%ROOT%\venv"
set "PYTHON_EXE=%VENV_DIR%\Scripts\python.exe"
set "REQS=%BACKEND_DIR%\requirements.txt"

set "CLI_ARG=%~1"
set "RUN_MODE="

if /I "%CLI_ARG%"=="--dev"          set "RUN_MODE=DEV"
if /I "%CLI_ARG%"=="-d"             set "RUN_MODE=DEV"
if /I "%CLI_ARG%"=="--prod"         set "RUN_MODE=PROD"
if /I "%CLI_ARG%"=="-p"             set "RUN_MODE=PROD"
if /I "%CLI_ARG%"=="--backend"      set "RUN_MODE=BACKEND"
if /I "%CLI_ARG%"=="--backend-only" set "RUN_MODE=BACKEND"
if /I "%CLI_ARG%"=="-b"             set "RUN_MODE=BACKEND"
if /I "%CLI_ARG%"=="--seed"         set "RUN_MODE=SEED_ONLY"

cls
echo.
echo  ========================================================================
echo    NyayaSetu - Digital Justice ^& Undertrial Rehabilitation Platform
echo    Bridging the Gap Between Justice and Access
echo  ========================================================================
echo.

:: -------------------------------------------------------
:: INTERACTIVE MENU IF NO ARGUMENT PROVIDED
:: -------------------------------------------------------
if "%RUN_MODE%"=="" (
    echo  Please choose how you would like to run NyayaSetu:
    echo.
    echo    [1] Production Mode  - Single Unified Server ^(Django serves React build^)
    echo    [2] Development Mode - Live HMR Frontend ^(Vite on :5173 + Django on :8000^)
    echo    [3] Backend API Only - Django REST Framework API ^(:8000^)
    echo    [4] Re-seed Database - Reset and reload rich demo data
    echo    [5] Exit
    echo.
    set /p "CHOICE=Enter choice (1-5, default is 1): "
    if "!CHOICE!"=="" set "CHOICE=1"
    if "!CHOICE!"=="1" set "RUN_MODE=PROD"
    if "!CHOICE!"=="2" set "RUN_MODE=DEV"
    if "!CHOICE!"=="3" set "RUN_MODE=BACKEND"
    if "!CHOICE!"=="4" set "RUN_MODE=SEED_ONLY"
    if "!CHOICE!"=="5" exit /b 0
)

echo.
echo [Selected Mode: !RUN_MODE!]
echo.

:: -------------------------------------------------------
:: STEP 1: Check Python System Installation
:: -------------------------------------------------------
echo [1/6] Checking Python runtime environment...

set "SYS_PYTHON="
where python >nul 2>&1
if !errorlevel! equ 0 (
    set "SYS_PYTHON=python"
) else (
    where py >nul 2>&1
    if !errorlevel! equ 0 (
        set "SYS_PYTHON=py -3"
    )
)

if not defined SYS_PYTHON (
    if not exist "%PYTHON_EXE%" (
        echo.
        echo [ERROR] Python was not found in your system PATH.
        echo         Please install Python 3.10+ from https://www.python.org/downloads/
        echo         * IMPORTANT: Make sure to check "Add Python to PATH" during installation.
        echo.
        pause
        exit /b 1
    )
) else (
    for /f "tokens=*" %%v in ('!SYS_PYTHON! --version 2^>^&1') do set "PY_VER=%%v"
    echo        Detected: !PY_VER!
)

:: -------------------------------------------------------
:: STEP 2: Create / Verify Virtual Environment
:: -------------------------------------------------------
echo [2/6] Verifying Python virtual environment (venv)...

if not exist "%PYTHON_EXE%" (
    echo        Creating virtual environment at "%VENV_DIR%" ...
    !SYS_PYTHON! -m venv "%VENV_DIR%"
    if !errorlevel! neq 0 (
        echo [ERROR] Failed to create virtual environment. Please verify Python installation.
        pause
        exit /b 1
    )
    echo        Virtual environment initialized.
) else (
    echo        Virtual environment located at venv - OK.
)

:: -------------------------------------------------------
:: STEP 3: Install Python Dependencies
:: -------------------------------------------------------
echo [3/6] Checking Python packages in requirements.txt...

if not exist "%REQS%" (
    echo [ERROR] requirements.txt not found at: %REQS%
    pause
    exit /b 1
)

"%PYTHON_EXE%" -m pip install --upgrade pip >nul 2>&1
"%PYTHON_EXE%" -m pip install -r "%REQS%" >nul 2>&1
if !errorlevel! neq 0 (
    echo        Retrying package installation with console output...
    "%PYTHON_EXE%" -m pip install -r "%REQS%"
    if !errorlevel! neq 0 (
        echo.
        echo [ERROR] Failed to install Python dependencies. Check internet connection.
        pause
        exit /b 1
    )
)
echo        Python dependencies are up to date.

:: -------------------------------------------------------
:: STEP 4: Check Node.js and Frontend Setup (if not BACKEND only)
:: -------------------------------------------------------
if not "!RUN_MODE!"=="BACKEND" if not "!RUN_MODE!"=="SEED_ONLY" (
    echo [4/6] Checking Node.js and building frontend...
    
    where node >nul 2>&1
    if !errorlevel! neq 0 (
        echo [WARNING] Node.js is not installed or not in PATH.
        echo           If frontend is already built, Django will serve existing dist directory.
        echo           Install Node.js 18+ from https://nodejs.org for Vite dev server or builds.
    ) else (
        for /f "tokens=*" %%v in ('node --version 2^>^&1') do set "NODE_VER=%%v"
        echo        Detected Node.js !NODE_VER!
        
        cd /d "%FRONTEND_DIR%"
        if not exist "node_modules" (
            echo        Installing npm packages...
            call npm install
            if !errorlevel! neq 0 (
                echo [ERROR] npm install encountered an error.
                pause
                exit /b 1
            )
        )
        
        if "!RUN_MODE!"=="PROD" (
            echo        Compiling production React bundle...
            call npm run build
            if !errorlevel! neq 0 (
                echo [ERROR] Frontend build failed. Check TypeScript and Vite output above.
                pause
                exit /b 1
            )
            echo        React production build compiled into dist directory.
        )
    )
) else (
    echo [4/6] Skipping frontend build.
)

:: -------------------------------------------------------
:: STEP 5: Database Migrations & Demo Seeding
:: -------------------------------------------------------
echo [5/6] Setting up database and rich demo accounts...
cd /d "%BACKEND_DIR%"

echo        Running database migrations...
"%PYTHON_EXE%" manage.py migrate --run-syncdb
if !errorlevel! neq 0 (
    echo [ERROR] Django database migration failed.
    pause
    exit /b 1
)

echo        Seeding categorized demo data across all modules...
"%PYTHON_EXE%" manage.py seed_demo
if !errorlevel! neq 0 (
    echo [ERROR] Demo data seeding failed.
    pause
    exit /b 1
)

if "!RUN_MODE!"=="SEED_ONLY" (
    echo.
    echo ========================================================================
    echo   Database has been successfully seeded with rich demo data!
    echo ========================================================================
    pause
    exit /b 0
)

:: -------------------------------------------------------
:: STEP 6: Server Launch & Credentials Display
:: -------------------------------------------------------
echo [6/6] Launching server...
echo.
echo  ========================================================================
echo    DEMO LOGIN CREDENTIALS
echo  ========================================================================
echo    Role               Email                       Password
echo    ----------------------------------------------------------------------
echo    Super Admin        admin@nyayasetu.demo        Admin@12345
echo    UTRC Authority     utrc@nyayasetu.demo         Utrc@12345
echo    Lawyer / Defense   lawyer@nyayasetu.demo       Lawyer@12345
echo    Human Rights Adv   lawyer2@nyayasetu.demo      Lawyer@12345
echo    DLSA Counsel       lawyer3@nyayasetu.demo      Lawyer@12345
echo    Prison Authority   prison@nyayasetu.demo       Prison@12345
echo    Rehab Staff / NGO  rehab@nyayasetu.demo        Rehab@12345
echo    Undertrial (Theft) undertrial@nyayasetu.demo   Undertrial@12345
echo    Undertrial(Assault)undertrial2@nyayasetu.demo  Undertrial@12345
echo    Support Person     support@nyayasetu.demo      Support@12345
echo  ========================================================================
echo.

cd /d "%BACKEND_DIR%"

if "!RUN_MODE!"=="DEV" (
    echo  [MODE: FULL DEVELOPMENT]
    echo  - Backend Django API Server : http://127.0.0.1:8000
    echo  - Vite Frontend Dev Server   : http://localhost:5173
    echo.
    echo  Launching Django and Vite in separate console windows...
    start "NyayaSetu - Django API [8000]" cmd /k "cd /d "%BACKEND_DIR%" && "%PYTHON_EXE%" manage.py runserver 8000"
    start "NyayaSetu - Vite Frontend [5173]" cmd /k "cd /d "%FRONTEND_DIR%" && npm run dev"
    
    timeout /t 3 >nul 2>&1
    start http://localhost:5173
    
    echo.
    echo  Both servers are running. Close the opened terminal windows to stop.
    echo.
    pause
    exit /b 0

) else if "!RUN_MODE!"=="BACKEND" (
    echo  [MODE: BACKEND API ONLY]
    echo  API Base URL: http://127.0.0.1:8000/api/
    echo  Admin Portal: http://127.0.0.1:8000/django-admin/
    echo.
    echo  Starting Django server on http://127.0.0.1:8000 - Press Ctrl+C to stop
    echo.
    "%PYTHON_EXE%" manage.py runserver 8000

) else (
    echo  [MODE: PRODUCTION UNIFIED SERVER]
    echo  Application Portal: http://127.0.0.1:8000
    echo  Django is serving the React frontend and REST APIs.
    echo.
    timeout /t 2 >nul 2>&1
    start http://127.0.0.1:8000
    echo  Starting production server - Press Ctrl+C to stop
    echo.
    "%PYTHON_EXE%" manage.py runserver 8000
)

endlocal
