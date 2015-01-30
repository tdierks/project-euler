
# Solve Hanayama Cast Box puzzle
#
# The puzzle is a cube with 12 edges. The ring is oriented originally around the START
# edge (edge A) and has an orientated pin in its opening.
#
# There are the following possible moves (and their inverses):
#  1. If the ring is off the puzzle entirely, it can be attached by slipping the
#     opening over an edge with a slot such that the pin is aligned with the slot
#  2. If the ring is around an edge and one of the four adjacent edges has a slot
#     aligned with the pin, the opening can be slipped over that edge to then place
#     the ring looped around the alternate adjacent edge
#  3. If the ring is around one edge, and a face-opposite edge has a compatible slot,
#     it can be slipped over that edge, after which it now loops the cube face-to-face,
#     and the ring can be moved to be over any adjacent set of edges.
#
# Edges are numbered as follows:
#   1 is the "start" edge: on the front-bottom
#   2, 3, and 4 are the bottom edges going clockwise (looking down)
#   5 is above and to the left of edge 1, followed by 6, 7, and 8 clockwise
#   9 is directly above "start" with 10, 11, 12 clockwise
#
#  face notations:
#   a - 1 2 3 4
#   b - 1 5 9 8
#   c - 2 6 10 5
#   d - 3 7 11 6
#   e - 4 8 12 7
#   f - 9 10 11 12
#
# When the ring is around an edge, it goes through two faces:
#  the 'in' face (pin points into it) and the 'out' face (pin points out of it)
#
# It can engage with the following slots: (all defined with the ring around the "near"
#   edge, with the gap intersecting the face)
#  on the 'in' face:
#   - the "top" of the near edge - removes ring
#   - the "top" of the left edge - move to connected
#   - the "top" of the right edge - move to connected
#   - the "top" of the far edge - to an axis loop
#  on the 'out' face:
#   - the "bottom" of the near edge - removes ring
#   - the "bottom" of the left/right edges - move to connected
#   - the "bottom" of the far edge - to axis loop
#

from collections import defaultdict
import re

def bidir(d):
  """ Add a reversed copy of the passed-in dict so k-v pairs are symmetric """
  bd = d.copy()
  for k, v in d.items():
    bd[v] = k
  return bd

faces_edges = { f: set(es) for f, es in {
  'a': [ '1', '2', '3', '4' ],
  'b': [ '1', '5', '9', '8' ],
  'c': [ '2', '6', '10', '5' ],
  'd': [ '3', '7', '11', '6' ],
  'e': [ '4', '8', '12', '7' ],
  'f': [ '9', '10', '11', '12' ],
}.items()}

opposite_faces = bidir({
  'a': 'f',
  'b': 'd',
  'c': 'e',
})

# These are the slot codes for the 7 slots in the puzzle. Each is the edge that the
# slot is on, followed by one of the faces and the slot's orientation with respect to
# that face: "inside" - on the inner edge of the face; "outside" - on the outer edge of
# the face, outside of the cube; "top" - on the surface of the face on the outside of the
# cube; "bottom" - on the underside of the face. Because each edge is on two faces, each
# slot has two codes, depending on which face it is considered with respect to. This
# list only contains one of the codes; the other is derived in paired_slot, below.
slot_codes = [
  '2ao',  # 2ct
  '4ao',  # 4et
  '5bi',  # 5cb
  '6cb',  # 6di
  '7di',  # 7eb
  '10ci',  # 10fb
  '12eb',  # 12fi
]

# ring state is a tuple of:
#   on edge: edge it's on, face we're considering, and whether pin is pointing in or out
#   on axis: which face we're considering, and pin pointing in or out

def parse_slot(slot):
  """ return a tuple of edge, face, and direction for a slot """
  m = re.match(r'^(\d+)(.)(.)$', slot)
  return m.group(1, 2, 3)

# reverses faces_edges into edge->faces map
edge_faces = defaultdict(set)
for f, es in faces_edges.items():
  for e in es:
    edge_faces[e].add(f)

def other_face(edge, face):
  """ given an edge and a face, return the other face for that edge """
  for f in edge_faces[edge]:
    if f != face:
      return f

def adjacent_edge(e1, e2):
  """ Given two edges, what is the third edge (if any) that meets at the corner where
  the two arguments intersect """
  common_faces = edge_faces[e1] & edge_faces[e2]
  if not common_faces:
    return None
  common_face = common_faces.pop()
  adj_edges = faces_edges[other_face(e1, common_face)] & faces_edges[other_face(e2, common_face)]
  if not adj_edges:
    return None
  return adj_edges.pop()

def all_edge_positions():
  """ return all single-edge position codes """
  for e in map(str, range(1,13)):
    for f in edge_faces[e]:
      for p in ['i', 'o']:
        yield e + f + p

# On the adjacent face, a top edge becomes an outside edge, etc.
paired_slot_codes = bidir({
  'o': 't',
  'i': 'b',
})

def paired_slot(slot):
  """ For a slot, return the matching slot name for its instance on the other face """
  s = parse_slot(slot)
  return s[0] + other_face(s[0], s[1]) + paired_slot_codes[s[2]]

# All the slots
slots = set(slot_codes).union({paired_slot(s) for s in slot_codes})

RING_OFF = '-'

opposite_direction = bidir({
  'i': 'o',
  't': 'b',
})

# when looking at slot in, given pin position, which slots do we care about:
#  top for in, bottom for out
face_slot_considered = {
  'i': 't',
  'o': 'b',
}

def all_transitions():
  """ Return a map of all possible moves in the game """
  transitions = defaultdict(set)

  # iterate over all on-edge positions
  for pos in all_edge_positions():
    pedge, pface, pdir = parse_slot(pos)

    # add other face considered (turning box to examine other face, no actual ring move)
    transitions[pos].add(pedge + other_face(pedge, pface) + opposite_direction[pdir])
    
    slot_dir = face_slot_considered[pdir]
    # consider passing the gap over each of the edges on the face being considered
    for edge in faces_edges[pface]:
      # if there's a slot on that edge that would allow the current pin position to pass
      if edge + pface + slot_dir in slots:
        if edge == pedge:
          # We can pass over the edge we're looped on -> transition to RING_OFF
          transitions[pos].add(RING_OFF)
        else:
          # this is a left/right edge if the ring position's edge and the edge under
          # consideration intersect at a corner (and thus have an adjacent edge)
          adj_edge = adjacent_edge(edge, pedge)
          if adj_edge:
            # you can pass the ring over to the adjacent edge
            transitions[pos].add(adj_edge + other_face(edge, pface) + pdir)
          else:
            # you can pass the ring to encircle two edges (on axis)
            transitions[pos].add(other_face(edge, pface) + pdir)

  # join axis faces: each axis face can be flipped to consider the opposite face
  for f in faces_edges.keys():
    transitions[f + 'i'].add(opposite_faces[f] + 'o')

  # all transitions are bidirectional, make sure they're all mapped
  for pos, next_poss in transitions.items():
    for next_pos in next_poss:
      transitions[next_pos].add(pos)

  return transitions

def search_in(transitions, visited, path, pos, goal):
  """ Recursive helper for depth-first search. Takes transition map, set of visited
    positions, list of path thus far, the next step to consider, and a goal. Returns
    a complete path to goal or None if no path found from this start state. """
  # If we're about to go someplace we've been, it's a loop: no path to goal
  if pos in visited:
    return None
  # Add pos to visited locations and path thus far
  visited.add(pos)
  path.append(pos)
  # If pos is the goal, we're done
  if pos == goal:
    return path
  # For each adjacent position, try moving there
  for next in transitions[pos]:
    r = search_in(transitions, visited, path, next, goal)
    if r:
      return r
  # If we get here, none of these led to the goal, so pos is a bad path, retrace by
  # removing pos from path & visited, then returning failure
  path.pop()
  visited.remove(pos)
  return None
    
def search(transitions, start, end):
  """ Depth-first search from start to end given transition map """
  return search_in(transitions, set(), [], start, end)
  
transitions = all_transitions()
path = search(transitions, '-', '1bi') or search(transitions, '-', '1bo')
print ", ".join(path)