# Epal Cheatsheet


# Component prefabs

## Utility components
| Component | Description | Data | Member functions | Requires components | Arguments |
| --------- | ----------- | ---- | ---------------- | ------------------- | --------- |
| epal.Transform | Stores positional data for an entity | <li>scale : epal.Vector2</li><li>position : epal.Vector2</li> |  |  |
| epal.AudioPlayer | Enables playing audio on one of the audio channels | <li>clips : list[epal.Asset]</li> <li>playing : bool</li> <li>track : str</li> <li>channel_id : int</li> | <li>add_clip(clip : epal.Asset or str)</li> <li>play_track(track : str)</li> <li>play()</li> <li>next()</li> <li>pause()</li> <li>stop()</li> <li>fadeout(time : int)</li> <li>toggle()</li> |  |  |

## Rendering components
| Component | Description | Data | Member functions | Requires components | Arguments |
| --------- | ----------- | ---- | ---------------- | ------------------- | --------- |
| epal.Rect | Enables rendering of a rect for that entity | <li>color : epal.Color</li> | | <li>epal.Transform</li> |  |
| epal.Circle | Enables rendering of a circle for that entity, radius is the x component of the scale | <li>color : epal.Color</li> |  | <li>epal.Transform</li> |  |
| epal.Ellipse | Enables rendering of a ellipse for that entity | <li>color : epal.Color</li> |  | <li>epal.Transform</li> |  |
| epal.Image | Enables rendering of a image for that entity | <li>color : epal.Color</li> <li>asset : epal.Asset or str</li> |  | <li>epal.Transform</li> | <li>asset : epal.Asset or str</li> |
| epal.Text | Enables multiline text rendering for the entity | <li>surface : pygame.Surface</li><li>text : str</li><li>font_object : epal.Font</li><li>color : epal.Color</li><li>background : epal.Color</li><li>position : epal.Vector2</li> | | | <li>text : str</li> |