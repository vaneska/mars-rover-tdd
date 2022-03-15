export type Position = {
  x: number;
  y: number;
  direction: "N" | "S" | "E" | "W";
};

export type Grid = {
  x: number; // Horizontal size. E.g. 10 means range [0..9] of positions
  y: number; // Vertical size. E.g. 10 means range [0..9] of positions
  obstacles?: Array<{ x: number; y: number }>;
};

export type World = {
  grid: Grid;
  position: Position; // Rover initial position
};
