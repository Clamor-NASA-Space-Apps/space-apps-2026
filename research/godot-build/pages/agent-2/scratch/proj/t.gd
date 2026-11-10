extends SceneTree
var n := 0
func _initialize():
	print("display=", DisplayServer.get_name(), " method=", RenderingServer.get_current_rendering_method(), " driver=", RenderingServer.get_current_rendering_driver_name())
func _process(_d):
	n += 1
	print("frame ", n, " engine_frames=", Engine.get_process_frames())
	if n == 2:
		var tex := root.get_texture()
		var img: Image = tex.get_image() if tex else null
		print("image=", img, " empty=", (img == null or img.is_empty()))
	return false
func _finalize():
	print("finalize after ", n, " process calls")
