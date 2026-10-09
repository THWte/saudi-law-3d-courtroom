export const ROLES=new Set(['judge','prosecutor','defense','witness']);
export const ACTIONS=new Set(['stand','sit','speak','listen','read','enter']);
export function normalizeEvent(x){if(!x||!ROLES.has(x.role)||!ACTIONS.has(x.action))throw new Error('Invalid presentation event');return {role:x.role,action:x.action};}
export function attachCourtEvents(pipeline,target=window){const handler=e=>{try{const x=normalizeEvent(e.detail);pipeline.perform(x.role,x.action);}catch(err){console.warn('Rejected presentation event',err.message);}};target.addEventListener('mizan:court-action',handler);return ()=>target.removeEventListener('mizan:court-action',handler);}
