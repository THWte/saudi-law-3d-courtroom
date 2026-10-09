// Timed visual speech cues. Requires model-specific morph targets and manually authored cues.
// Does not analyze Arabic audio or infer phonemes.
export function validateSpeechCues(cues){
  if(!Array.isArray(cues)||cues.length>2000)throw new Error('Invalid cue list');
  let previous=-1;
  return cues.map(c=>{
    if(!c||!Number.isFinite(c.at)||c.at<0||c.at<previous||typeof c.morph!=='string'||!/^[a-zA-Z0-9_-]{1,64}$/.test(c.morph)||!Number.isFinite(c.weight)||c.weight<0||c.weight>1)throw new Error('Invalid speech cue');
    previous=c.at;return {at:c.at,morph:c.morph,weight:c.weight};
  });
}
export class SpeechCuePlayer{
  constructor(pipeline){this.pipeline=pipeline;this.active=new Map();}
  start(role,cues,now=performance.now()){const validated=validateSpeechCues(cues);this.stop(role);this.active.set(role,{cues:validated,index:0,start:now,last:null});}
  stop(role){const s=this.active.get(role);if(s?.last)this.pipeline.setExpression(role,s.last,0);this.active.delete(role);}
  tick(now=performance.now()){for(const [role,s] of this.active){const elapsed=(now-s.start)/1000;while(s.index<s.cues.length&&s.cues[s.index].at<=elapsed){const cue=s.cues[s.index++];if(s.last&&s.last!==cue.morph)this.pipeline.setExpression(role,s.last,0);this.pipeline.setExpression(role,cue.morph,cue.weight);s.last=cue.morph;}if(s.index===s.cues.length&&elapsed>(s.cues.at(-1)?.at??0)+.2)this.stop(role);}}
}
