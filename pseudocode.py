
def state_update(imperative_correspondances, prior)
	new = function?(imperative_correspondances)
	k = prior * new 
	return k

def factual_factor(declarative_u, k, grounding_set):
	??
	return factual_correspondances

def sentence_tracker(declarative_u, k, detections, grounding_set):
	#existencial and conceptual groundigs
	parse = parse(declarative_u)
	
	for i in xrange(participants(parse)):
		HMM_tracker = ??max(high detection + high coherence)

	for i in xrange(groundings(parse)):	
	HMM_grounding =	???(HMM_tracker)

	perceptual_
	existential_
	return declarative_correspondances
	

def dcg(impreative_u, declarative_correspondances, grounding_set):	
	treelike_order
	features(lexical cues, spatial characteristics, child groundings)
	log linear 
	search using beam search

	goals_
	constraints_

image= get_image()
utterance = get_utterance()
grounding_set=defined?
BinaryCorrespondanceSet=GroudningsxUtterance

#For every frame
detections = detections.append(detect(image))

BinaryPerceptualCorrespondanceSet=detectionxWorldModel

#Inference:
if utterance:
	declarative_u, imperative_u, dependencies/tree = parser(utterance)

	factual_correspondances = factual_factor(declarative_u, k, grounding_set)

	declarative_correspondances = sentence_tracker(declarative_u, detections, grounding_set)

	imperative_correspondances = dcg(imperative_u, declarative_correspondances, grounding_set)?

	k= state_update(imperative_correspondances, k)

	control_sequence = planner(imperative_correspondances)

	execute(control_sequence)


#Training
dcg:
	beam search, feature vectors
sentence_tracker:
	EM
