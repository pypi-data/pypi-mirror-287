from upyrc import upyre

# Optional, to have more verbose log
import logging
upyre.set_log_level(logging.DEBUG)

PROJECT_FOLDER = "D:/Projects/UpyreTest/UnrealRemoteControlTestData"
# ==> Change it for your test project path.

# Set your project path here, it will fetch the python settings of your project, but your MUST have the "Enable remote execution" of the python plugin enabled in unreal.
config = upyre.RemoteExecutionConfig.from_uproject_path(f"{PROJECT_FOLDER}/UpyreTest.uproject")

# Create the connection
with upyre.PythonRemoteConnection(config) as conn:
    
    # Example with a file path
    conn.import_fbx_static_meshes(["T:/H_to_EU_FBX/pigtest01.fbx"], "/Game/FBXImportTest")