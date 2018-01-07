/*
s180106 Platonic Solids
(c)2018 Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
*/

PlatonicSolid[] solids;
float r_x = 0;
float r_y = 0;

void setup() {
  size(500, 500, P3D);
  strokeCap(ROUND);
  smooth();
  solids = new PlatonicSolid[100];
  for (int i = 0; i<100; i++) {
    switch((int)random(5)) {
    case 0:  
      solids[i] = new Tetrahedron(18, false); 
      break;
    case 1:  
      solids[i] = new Hexahedron(14, false);
      break;
    case 2:  
      solids[i] = new Octahedron(22, false);    
      break;
    case 3:  
      solids[i] = new Dodecahedron(18, false);    
      break;
    case 4:  
      solids[i] = new Icosahedron(18, false);    
      break;
    }
  }
}

void draw() {
  r_x += 0.02;
  r_y += 0.01;
  background(0);
  lights();
  stroke(200, 0, 0);
  strokeWeight(3);

  for (int i = 0; i<100; i++) {
    int x = x_from_i(i, 10, 10);
    int y = y_from_i(i, 10, 10);
    pushMatrix();
    translate(25 + x *50, 25 + y *50);

    pushMatrix(); 
    pushStyle();
    if (dist(mouseX, mouseY, 25 + x *50, 25 + y *50)<25) {
      scale(2);
      translate(0, 0, 30);
      stroke(255);
    }
    rotateX(r_y);
    rotateY(r_x);
    solids[i].create();
    popStyle();
    popMatrix();
    popMatrix();
  }
}

int x_from_i(int idx, int max_x, int max_y) {
  int x =  idx % max_x;
  return x;
}

int y_from_i(int idx, int max_x, int max_y) {
  idx /= max_x;
  int y = idx % max_y;
  return y;
}