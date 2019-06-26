module Torus(major, minor) {
    rotate_extrude(convexity = 10, $fn=100)
    translate([major, 0, 0])
    circle(r = minor, $fn = 100);
}

scale([3.0, 3.0, 3.0]) {
    rotate(90.0, [1.0, 0.0, 0.0]) {
    translate([0.0, 0.0, 50.0]) {
    mirror([1.0, 1.0, 0.0]) {
    difference() {
    intersection() {
    cube([20.0, 20.0, 20.0], center=true);
    sphere(r = 20.0, $fn=100);
    polyhedron(
    points=[ [10.0,10.0,-10.0], [10.0,-10.0,-10.0],
             [-10.0,-10.0,-10.0], [-10.0,10.0,-10.0], [0,0,0] ],
    faces=[ [0,1,4], [1,2,4], [2,3,4], [3,0,4], [1,0,3], [2,1,3] ]
);
}
    union() {
    translate([0.0, 0.0, -10.0]) {cylinder(h = 20.0,  r1 = 20.0, r2=0,  $fn=100, center=true);}
    cylinder(h = 10.0, r = 20.0, $fn=100, center=true);
    Torus(30.0, 20.0);
}
}
}
}
}
}
