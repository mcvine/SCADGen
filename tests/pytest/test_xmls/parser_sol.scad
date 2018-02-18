union() {
    cylinder(h = 5, r = 2.5, $fn=100);
    translate([0.0, 0.0, -2.5]) {
    cylinder(h = 10, r = 15, $fn=100);
}
}
