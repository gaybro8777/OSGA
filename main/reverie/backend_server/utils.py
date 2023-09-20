openai_api_key = "something" # Can use anything within the string if not actually using OpenAI_API (however there must be "some" string)

"""use ngrok for public IP addresses of externally hosted notebook instances (uncomment and comment out the line for local llama)"""
# base_api_url = "http://c5b0-34-171-95-246.ngrok-free.app/v1"   #   "https://YOUR_NEW_API_ENDPOINT/v1" must end in /v1 due to the nature of llama-cpp-python

"""use localhost for local llama (uncomment and comment out the line for ngrok)"""
base_api_url = "http://localhost:8080/v1" # Use for local llama


maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose 
debug = True

debug_scratch = 20
debug_run_gpt_prompt = 20

# Pick level of debugging (level picked includes everything to the right of it):
# DEBUG[10]->INFO[20]->WARNING[30]->ERROR[40]->CRITICAL[50]