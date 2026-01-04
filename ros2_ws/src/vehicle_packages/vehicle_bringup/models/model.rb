require 'erb'

# Get command-line arguments
robot_name = ARGV[0] || "default_robot_name"
erb_path = ARGV[1] || "default_erb_path"
sdf_path = ARGV[2] || "default_sdf_path"
robot_x = ARGV[3] || "5.0"
robot_y = ARGV[4] || "5.0"

robot_name_with_slash =
  robot_name.to_s.strip.empty? ? "" : "#{robot_name}/"

# Prepare variables hash
variables = {
  robot_name: robot_name,
  robot_name_with_slash: robot_name_with_slash,
  robot_x: robot_x,
  robot_y: robot_y,
}

# Load and process the ERB template
template_file = File.read(erb_path)
template = ERB.new(template_file)
result = template.result_with_hash(variables)

# Output or save the result
File.write(sdf_path, result)