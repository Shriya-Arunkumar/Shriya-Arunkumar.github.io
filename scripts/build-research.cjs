// Shared factual project summaries for the default and optional application pages.
// Edit research-content.json, then run: node scripts/build-research.cjs
const fs=require('fs');
const {direction,projects}=JSON.parse(fs.readFileSync('scripts/research-content.json','utf8'));
const template=fs.readFileSync('projects/robot-attention.html','utf8');
for(const slug of ['', 'epfl','eth','ntu','nus']){
 const prefix=slug?'../../':'../';
 const title=slug?`Research interests — ${slug.toUpperCase()}`:'Research interests';
 let page=template.replaceAll('../',prefix).replace(/<title>.*?<\/title>/,`<title>${title} | Shriya Arunkumar</title>`).replace(/<meta name="description" content="[^"]*">/,`<meta name="description" content="${direction}">`);
 const body=`<a class="text-link back-link" href="${prefix}index.html#research">← Portfolio</a><header class="project-intro"><p class="eyebrow">Research direction</p><h1 class="editorial-title">${title}</h1><p class="project-lead">${direction}</p></header><section class="story-section"><h2>Current themes</h2><p>Robust autonomous navigation, perception under uncertain sensing, and reconfigurable robotic systems. My completed HRI internship provides experience connecting perception to simulated robot behavior.</p></section><div class="project-grid">${projects.map(p=>p.replaceAll('projects/',prefix+'projects/').replaceAll('src="assets/','src="'+prefix+'assets/')).join('')}</div>`;
 page=page.replace(/(<main id="main" class="container project-page">)[\s\S]*?(<\/main>)/,`$1${body}$2`);
 fs.mkdirSync('research/'+slug,{recursive:true});fs.writeFileSync('research/'+(slug?slug+'/':'')+'index.html',page);
}
