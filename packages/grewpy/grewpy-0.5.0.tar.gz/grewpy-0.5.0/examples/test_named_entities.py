import sys, os, json

sys.path.insert(0, os.path.abspath(os.path.join( os.path.dirname(__file__), "../"))) # Use local grew lib

from grewpy import Request
r = Request() #.pattern("e: N -[1=subj]-> M; N[upos=VERB]").without("M[upos=NOUN]")
print (r.named_entities())
