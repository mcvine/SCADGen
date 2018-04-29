union() {
    cylinder(h = 5.0, r = 2.5, $fn=100, center=true);
    translate([0.0, 0.0, -2.5]) {
    cylinder(h = 10.0, r = 1.5, $fn=100, center=true);
}
}
