import { test, expect } from "@playwright/test";

const grid_2x2 = { x: 2, y: 2 };
const grid_2x2_w_obstacle_at_1_1 = { x: 2, y: 2, obstacles: [{ x: 1, y: 1 }] };
const grid_10x10 = { x: 10, y: 10 };
const _0_0_N = { x: 0, y: 0, direction: "N" };

test.describe("Rover final spec", () => {
  test("first command returns next rover position", async ({ request }) => {
    await roverAt(_0_0_N, grid_10x10, request);

    const addCommandResponse = await addCommand(request, "MMRMMLM");

    expect(addCommandResponse.status()).toBe(201);
    const { point } = await addCommandResponse.json();
    expect(point).toMatchObject({ x: 2, y: 3, direction: "N" });
  });

  test("multiple commands sum up final position", async ({ request }) => {
    await roverAt(_0_0_N, grid_2x2, request);

    await addCommand(request, "MR");
    const secondCommandResponse = await addCommand(request, "M");

    expect(secondCommandResponse.status()).toBe(201);
    const { point } = await secondCommandResponse.json();
    expect(point.x).toMatchObject({ x: 1, y: 1, direction: "E" });
  });

  test("rover declines command if path crosses grid boundaries", async ({
    request,
  }) => {
    await roverAt(_0_0_N, grid_2x2, request);

    await addCommand(request, "M");
    const badCommandResponse = await addCommand(request, "M");

    expect(badCommandResponse.status()).toBe(400);
    const { error } = await badCommandResponse.json();
    expect(error).toBe("unable to cross grid boundary");
  });

  test("rover declines command if path goes through obstacle", async ({
    request,
  }) => {
    await roverAt(_0_0_N, grid_2x2_w_obstacle_at_1_1, request);

    await addCommand(request, "MR");
    const badCommandResponse = await addCommand(request, "M");

    expect(badCommandResponse.status()).toBe(400);
    const { error } = await badCommandResponse.json();
    expect(error).toBe("unable to pass through the obstacle");
  });
});

const roverAt = (position, grid, request) =>
  request.put("/map", { data: { position, grid } });

const addCommand = (request, command: string) =>
  request.post(`/command`, { data: { command } });
