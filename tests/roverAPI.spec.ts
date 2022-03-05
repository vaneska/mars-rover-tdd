import { test, expect } from "@playwright/test";

test.describe("Rover final spec", () => {
  test("first command returns next rover position", async ({ request }) => {
    await roverIs_0_0_N_at_10x10_grid(request);

    const addCommandResponse = await addCommand(request, "MMRMMLM");

    expect(addCommandResponse.status()).toBe(201);
    const { point } = await addCommandResponse.json();
    expect(point).toMatchObject({ x: 2, y: 3, direction: "N" });
  });
  test("multiple commands sum up final position", async ({ request }) => {
    await roverIs_0_0_N_at_10x10_grid(request);

    await addCommand(request, "MR");
    const secondCommandResponse = await addCommand(request, "M");

    expect(secondCommandResponse.status()).toBe(201);

    const { point } = await secondCommandResponse.json();
    expect(point.x).toMatchObject({ x: 1, y: 1, direction: "E" });
  });
});

const grid_10x10 = { x: 10, y: 10 };
const position_0_0_N = { x: 0, y: 0, direction: "N" };

async function roverIs_0_0_N_at_10x10_grid(request) {
  await request.put("/map", {
    data: { size: grid_10x10, position: position_0_0_N },
  });
}

async function addCommand(request, command: string) {
  return await request.post(`/command`, {
    data: { command },
  });
}
