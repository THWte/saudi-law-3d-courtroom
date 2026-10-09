// Local-only audio envelope -> generic mouthOpen morph. Not phoneme/viseme recognition.
export function envelopeToCues(samples,sampleRate,{morph='mouthOpen',fps=10,gain=8}={}){
  if(!(samples instanceof Float32Array)||!Number.isFinite(sampleRate)||sampleRate<=0||samples.length>sampleRate*180||!Number.isFinite(fps)||fps<1||fps>60)throw new Error('Invalid audio envelope input');
  if(!/^[a-zA-Z0-9_-]{1,64}$/.test(morph))throw new Error('Invalid morph name');
  const stride=Math.max(1,Math.round(sampleRate/fps)),cues=[];
  for(let start=0;start<samples.length;start+=stride){let sum=0;const end=Math.min(start+stride,samples.length);for(let i=start;i<end;i++){const x=Number.isFinite(samples[i])?samples[i]:0;sum+=x*x;}const rms=Math.sqrt(sum/(end-start));cues.push({at:start/sampleRate,morph,weight:Math.min(1,Math.max(0,rms*gain))});}
  cues.push({at:samples.length/sampleRate,morph,weight:0});
  return cues;
}
export async function decodeLocalAudio(file,audioContext){
  if(!file||file.size>20*1024*1024||!/^audio\//.test(file.type))throw new Error('Only audio files up to 20 MB');
  const buffer=await audioContext.decodeAudioData(await file.arrayBuffer());
  const samples=new Float32Array(buffer.length);
  for(let channel=0;channel<buffer.numberOfChannels;channel++){const data=buffer.getChannelData(channel);for(let i=0;i<data.length;i++)samples[i]+=data[i]/buffer.numberOfChannels;}
  return {samples,sampleRate:buffer.sampleRate};
}
