import { test, expect } from "@playwright/test";

test.describe("add command endpoint", () => {
  test("should return next rover position", async ({ request }) => {
    const addCommandResponse = await request.post(`/command`, {
      data: { command: "MMRMMLM" },
    });

    expect(addCommandResponse.status()).toBe(201);

    const { point } = await addCommandResponse.json();
    expect(point.x).toBe(2);
    expect(point.y).toBe(3);
    expect(point.direction).toBe("N");
  });
});
