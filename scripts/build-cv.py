from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from pathlib import Path
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='NameCV',fontName='Helvetica-Bold',fontSize=24,leading=28,textColor=HexColor('#182333'),spaceAfter=8))
styles.add(ParagraphStyle(name='SectionCV',fontName='Helvetica-Bold',fontSize=11,leading=14,textColor=HexColor('#1b4fd8'),spaceBefore=13,spaceAfter=6))
styles.add(ParagraphStyle(name='TextCV',fontName='Helvetica',fontSize=9,leading=12,spaceAfter=5))
story=[]
def p(t,style='TextCV'): story.append(Paragraph(t,styles[style]))
def section(t): p(t,'SectionCV')
p('Shriya Arunkumar','NameCV')
p('Autonomous Navigation | Robotic Perception | Reconfigurable Robotics')
p('<link href="mailto:arunkumarshriya@gmail.com">arunkumarshriya@gmail.com</link> | Bengaluru, India<br/><link href="https://github.com/Shriya-Arunkumar">github.com/Shriya-Arunkumar</link> | <link href="https://www.linkedin.com/in/shriya-arunkumar/">LinkedIn: shriya-arunkumar</link>')
section('EDUCATION')
p('<b>PES University, Bengaluru</b> | Expected graduation: 2028<br/>B.Tech, Electronics and Communication Engineering | CGPA: 8.50/10<br/>Minor in Computer Science | CGPA: 9.00/10')
section('RESEARCH EXPERIENCE')
p('<b>Summer Research Intern - cRAIS, PES University</b> | Summer 2026<br/>Human-Robot Interaction, Gaze Estimation, Robot Attention')
p('Developed a webcam-based multi-person robot attention software prototype connecting face and gaze estimation, object-level attention reasoning, confidence-aware inference, and attention arbitration to ROS2 and Gazebo robot-eye simulation. Further algorithm refinement and experimental evaluation are planned.')
p('<b>Research Intern - cRAIS, PES University</b> | Current<br/>Working on a tri-modal robotic platform exploring mobility across land, air, and water. Focus: robotic systems design, CAD development, mechanical integration, and experimental research.')
section('SELECTED TECHNICAL PROJECTS')
p('<b>Multi-Person Robot Attention System</b> | Prototype implemented<br/>Integrated visual perception and attention selection with ROS2 Humble and Gazebo Classic. Python, OpenCV, MediaPipe, and C++ support the perception-to-simulation pipeline. Quantitative evaluation remains planned.')
p('<b>Trimodal Robot - Ongoing Research</b> | Design and development in progress<br/>An ongoing robotics research project investigating a robotic platform designed to operate across terrestrial, aerial, and aquatic environments. Further technical details are not publicly disclosed at this stage.')
p('<b>Autonomous Navigation for Indian Roads</b> | Research in progress<br/>Primary research responsibility: investigating adaptive multi-sensor fusion under varying sensor reliability and environmental uncertainty. Algorithm development is ongoing; simulation and experimental evaluation are planned.')
p('<b>Custom 5-DOF Robotic Arm</b> | Under development<br/>Designing an SO-101-inspired 3D-printed arm with an actuated gripper, modular mechanisms, and an Arduino/PCA9685 control architecture. Joint feedback, ROS2, and robot learning are future directions.')
p('<b>Dynamic Vision Sensor Simulator</b> | Software demonstration<br/>Python exploration of per-pixel brightness changes as event activity. Public source and demonstration are linked from the portfolio; physical-sensor benchmarking is not reported.')
section('TECHNICAL SKILLS')
p('<b>Programming:</b> Python, C++ | <b>Vision:</b> OpenCV, MediaPipe, gaze estimation, facial landmarks<br/><b>Robotics:</b> ROS2 Humble, Gazebo Classic, simulation integration<br/><b>Design:</b> Fusion 360, SolidWorks, mechanical assemblies, 3D modelling<br/><b>Embedded:</b> Arduino, servo control, electronics prototyping<br/><b>Research:</b> Literature review, technical documentation; developing evaluation and analysis methods')
section('SELECTED ACHIEVEMENTS')
p('DVS simulator: public software and demonstration. Research project documentation available at <link href="https://Shriya-Arunkumar.github.io">Shriya-Arunkumar.github.io</link>. No peer-reviewed publications listed.')
p('Parallax 3.0: 1st, 2025 | Hacksimulink: 2nd, September 2026<br/>Math Hackathon: 5th, 2025 | Riverie Hacks: 7th, 2024<br/>NOVA Residency: pitched a deeptech startup idea to 20+ investors.<br/>PES Women\'s Basketball Team: 3rd, Revels Cup 2026, MIT Manipal.')
SimpleDocTemplate('assets/Shriya-Arunkumar-CV.pdf',pagesize=(595.28,841.89),rightMargin=42,leftMargin=42,topMargin=32,bottomMargin=30,title='Shriya Arunkumar - Academic CV',author='Shriya Arunkumar').build(story)
